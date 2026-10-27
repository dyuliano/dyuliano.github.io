(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  const locale = document.documentElement.lang.startsWith('en') ? 'en-US' : 'pt-BR';
  const fmt = n => n.toLocaleString(locale);
  const ease = t => 1 - Math.pow(1 - t, 3);

  /* abertura: anos de carreira até o ano atual (uma vez por sessão) */
  const start = () => { document.body.classList.remove('loading'); document.body.classList.add('ready'); career(); };

  /* barra de carreira: marcador viaja de 2008 até o ano atual */
  function career() {
    const fill = $('#careerFill'), rider = $('#careerRider'); if (!fill) return;
    const yEl = $('b', rider), ticks = $$('.career .ticks span');
    const y0 = 2008, y1 = new Date().getFullYear();
    const set = p => {
      const w = (p * 100) + '%';
      fill.style.width = w; rider.style.left = w;
      yEl.textContent = Math.round(y0 + (y1 - y0) * p);
      ticks.forEach((t, i) => t.classList.toggle('on', p >= i / (ticks.length - 1) - .001));
    };
    if (reduce) { set(1); return; }
    set(0);
    setTimeout(() => {
      const t0 = performance.now(), d = 2200;
      const step = now => { const p = Math.min(1, (now - t0) / d); set(p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2); if (p < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    }, 900);
  }

  /* índices para entradas em sequência */
  $$('[data-stagger]').forEach(g => [...g.children].forEach((c, i) => c.style.setProperty('--i', i)));
  $$('.job ul, .ladder').forEach(g => [...g.children].forEach((c, i) => c.style.setProperty('--i', i)));
  $$('.pillar').forEach((p, i) => p.style.setProperty('--i', i));
  $$('.pillar .ic svg *').forEach(el => el.setAttribute('pathLength', '1'));
  const intro = $('#intro');
  let seen = false;
  try { seen = sessionStorage.getItem('introSeen') === '1'; sessionStorage.setItem('introSeen', '1'); } catch (e) {}
  if (!intro || reduce || seen) { intro && intro.remove(); start(); }
  else {
    const y0 = +intro.dataset.from, y1 = new Date().getFullYear(), t0 = performance.now(), dur = 1500;
    const yEl = $('.year', intro), bar = $('.bar i', intro);
    let finished = false;
    const finish = () => { if (finished) return; finished = true; intro.classList.add('done'); start(); setTimeout(() => intro.remove(), 1000); };
    const tick = now => {
      const p = Math.min(1, (now - t0) / dur), e = ease(p);
      yEl.textContent = Math.round(y0 + (y1 - y0) * e);
      bar.style.transform = `scaleX(${e})`;
      if (p < 1) requestAnimationFrame(tick); else setTimeout(finish, 250);
    };
    requestAnimationFrame(tick);
    setTimeout(finish, 3200);
  }
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  /* menu no celular */
  const nav = $('#nav'), mb = $('#menuBtn');
  const setMenu = open => {
    nav.classList.toggle('open', open);
    mb.setAttribute('aria-expanded', open);
    mb.setAttribute('aria-label', open ? mb.dataset.close : mb.dataset.open);
    document.body.style.overflow = open ? 'hidden' : '';
  };
  mb.addEventListener('click', () => setMenu(!nav.classList.contains('open')));
  $$('#menu a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

  /* progresso, menu ativo e trilho da linha do tempo */
  const prog = $('#progress'), tl = $('#tl'), rail = $('#railFill');
  const links = $$('#menu a'), secs = links.map(a => $(a.getAttribute('href')));
  const onScroll = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    prog.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
    if (tl) {
      const r = tl.getBoundingClientRect();
      rail.style.transform = `scaleY(${Math.min(1, Math.max(0, (innerHeight * .65 - r.top) / r.height))})`;
    }
    let cur = -1;
    secs.forEach((s, i) => { if (s && s.getBoundingClientRect().top < innerHeight * .35) cur = i; });
    if (max > 0 && scrollY >= max - 4) cur = secs.length - 1;
    links.forEach((a, i) => a.classList.toggle('active', i === cur));
  };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  onScroll();

  /* entrada das seções e contadores */
  const countUp = el => {
    const to = +el.dataset.to, pre = el.dataset.prefix || '';
    if (reduce) { el.textContent = pre + fmt(to); return; }
    const t0 = performance.now(), d = 1400;
    const step = now => { const p = Math.min(1, (now - t0) / d); el.textContent = pre + fmt(Math.round(to * ease(p))); if (p < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  };
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in'); io.unobserve(e.target);
    $$('[data-to]', e.target).forEach(countUp);
    $$('.mba', e.target).forEach(mba);
  }), { threshold: .15, rootMargin: '0px 0px -6% 0px' });
  $$('.reveal, .job, .kpis, [data-stagger]').forEach(el => io.observe(el));

  /* progresso real do MBA pela data de hoje */
  function mba(el) {
    const a = new Date(el.dataset.start), b = new Date(el.dataset.end), now = new Date();
    const p = Math.max(0, Math.min(1, (now - a) / (b - a)));
    $('i', el).style.width = (p * 100).toFixed(1) + '%';
    $('span', el).textContent = el.dataset.label.replace('{p}', Math.round(p * 100));
  }

  /* confirmação ao baixar o currículo */
  $$('[data-dl]').forEach(a => a.addEventListener('click', () => {
    const b = a.classList.contains('btn') ? a : null; if (!b) return;
    b.classList.add('downloaded'); clearTimeout(b._t);
    b._t = setTimeout(() => b.classList.remove('downloaded'), 2600);
  }));

  /* botão flutuante de currículo no celular */
  (() => {
    const fab = $('.fab'), hero = $('#inicio'), cv = $('#curriculo'); if (!fab) return;
    let heroOut = false, cvIn = false;
    const upd = () => fab.classList.toggle('show', heroOut && !cvIn);
    new IntersectionObserver(([e]) => { heroOut = !e.isIntersecting; upd(); }, { threshold: 0 }).observe(hero);
    new IntersectionObserver(([e]) => { cvIn = e.isIntersecting; upd(); }, { threshold: 0 }).observe(cv);
    new IntersectionObserver(([e]) => { if (e.isIntersecting) { cvIn = true; upd(); } }, { threshold: 0 }).observe($('#contato'));
  })();

  /* 400 → 1.500: clientes chegam das bordas e se ligam à mesma equipe */
  (() => {
    const c = $('#dots'); if (!c) return;
    const x = c.getContext('2d'), toEl = $('#scaleTo'), bar = $('#barGrow'), barV = $('#barV'), ratio = $('#ratio');
    const TOTAL = 1500, BASE = 400, T_BASE = 900, T_IN = 3400, FLY = 1000;
    const col = { base: css('--dot-base'), fresh: css('--dot-new'), empty: css('--dot-empty'), team: css('--team'), teamInk: css('--team-ink'), ink: css('--ink') };
    let W, H, cell, r, cx, cy, dots = [], t0 = null, visible = false, raf = 0, done = reduce;
    const layout = () => {
      const dpr = Math.min(devicePixelRatio || 1, 2); W = c.clientWidth; H = c.clientHeight;
      c.width = W * dpr; c.height = H * dpr; x.setTransform(dpr, 0, 0, dpr, 0, 0);
      const cols = Math.ceil(Math.sqrt(TOTAL * W / H)), rows = Math.ceil(TOTAL / cols);
      cell = Math.min(W / cols, H / rows); r = Math.max(1, cell * .28); cx = W / 2; cy = H / 2;
      const ox = (W - cols * cell) / 2, oy = (H - rows * cell) / 2, R = Math.hypot(W, H) * .62;
      dots = [];
      for (let i = 0; i < cols * rows && dots.length < TOTAL; i++) {
        const gx = ox + (i % cols + .5) * cell, gy = oy + (Math.floor(i / cols) + .5) * cell;
        if (Math.hypot(gx - cx, gy - cy) < cell * 3.6) continue;
        dots.push({ x: gx, y: gy, d: Math.hypot(gx - cx, (gy - cy) * 1.3) });
      }
      while (dots.length < TOTAL) dots.push({ ...dots[dots.length - 1] });
      dots.sort((a, b) => a.d - b.d);
      const maxD = dots[dots.length - 1].d;
      dots.forEach((d, i) => {
        d.i = i; d.nd = d.d / maxD;
        const a = Math.atan2(d.y - cy, d.x - cx) + (Math.random() - .5) * 1.4;
        d.sx = cx + Math.cos(a) * R; d.sy = cy + Math.sin(a) * R;
        d.ts = i < BASE ? d.nd * T_BASE : T_BASE + 200 + Math.pow((i - BASE) / (TOTAL - BASE), .85) * T_IN;
        d.j = Math.random() * 120;
      });
      if (!raf) draw(performance.now());
    };
    const dot = (px, py, rr, fill) => { x.fillStyle = fill; x.beginPath(); x.arc(px, py, rr, 0, 7); x.fill(); };
    const draw = now => {
      raf = 0;
      const t = done ? 1e9 : (t0 === null ? -1 : now - t0);
      x.clearRect(0, 0, W, H);
      let n = 0;
      x.lineWidth = .7;
      for (let k = BASE; k < TOTAL; k++) {
        const d = dots[k], at = t - (d.ts + FLY + d.j);
        if (at > 0 && at < 500) { x.globalAlpha = .35 * (1 - at / 500); x.strokeStyle = col.fresh; x.beginPath(); x.moveTo(cx, cy); x.lineTo(d.x, d.y); x.stroke(); }
      }
      x.globalAlpha = 1;
      for (const d of dots) {
        const lt = t - d.ts;
        if (d.i < BASE) {
          if (lt < 0) { dot(d.x, d.y, r, col.empty); continue; }
          n++; const k = Math.min(1, lt / 400);
          x.globalAlpha = .3 + .7 * k; dot(d.x, d.y, r * (1 + (1 - k) * .8), col.base); x.globalAlpha = 1;
          continue;
        }
        const ft = lt - d.j;
        if (ft < 0) { dot(d.x, d.y, r, col.empty); continue; }
        if (ft < FLY) {
          const p = ease(ft / FLY), q = ease(Math.max(0, ft / FLY - .14));
          const px = d.sx + (d.x - d.sx) * p, py = d.sy + (d.y - d.sy) * p, qx = d.sx + (d.x - d.sx) * q, qy = d.sy + (d.y - d.sy) * q;
          dot(d.x, d.y, r, col.empty);
          x.globalAlpha = .55; x.strokeStyle = col.fresh; x.lineWidth = r * 1.1; x.lineCap = 'round';
          x.beginPath(); x.moveTo(qx, qy); x.lineTo(px, py); x.stroke(); x.globalAlpha = 1; x.lineWidth = .7;
          dot(px, py, r * 1.1, col.fresh);
          continue;
        }
        n++;
        const af = ft - FLY, fl = af < 450 ? 1 - af / 450 : 0;
        dot(d.x, d.y, r * (1 + fl * 1.1), col.fresh);
      }
      const R0 = cell * 3.1, busy = t > T_BASE && t < T_BASE + T_IN + FLY + 400;
      if (busy) for (let k = 0; k < 3; k++) {
        const ph = ((now / 1400) + k / 3) % 1;
        x.globalAlpha = .5 * (1 - ph); x.strokeStyle = col.ink; x.lineWidth = 1; x.beginPath(); x.arc(cx, cy, R0 + ph * cell * 7, 0, 7); x.stroke();
      }
      x.globalAlpha = 1;
      dot(cx, cy, R0, col.team);
      x.strokeStyle = col.ink; x.lineWidth = 2; x.beginPath(); x.arc(cx, cy, R0, 0, 7); x.stroke();
      const spin = now / 9000;
      for (let k = 0; k < 7; k++) { const a = k / 7 * Math.PI * 2 + spin; dot(cx + Math.cos(a) * cell * 1.6, cy + Math.sin(a) * cell * 1.6, r * 1.3, col.teamInk); }
      const v = done ? TOTAL : Math.max(BASE, n);
      toEl.textContent = fmt(v); barV.textContent = fmt(v);
      bar.style.width = ((v - BASE) / TOTAL * 100) + '%';
      if (v >= TOTAL) { ratio.classList.add('on'); if (!done && t > T_BASE + T_IN + FLY + 500) done = true; }
      if (visible && !reduce && !done) raf = requestAnimationFrame(draw);
    };
    layout();
    let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(layout, 150); });
    new IntersectionObserver(([e]) => {
      visible = e.isIntersecting;
      if (visible && t0 === null && !reduce) t0 = performance.now() + 250;
      if (visible && !raf && !done) raf = requestAnimationFrame(draw);
    }, { threshold: .35 }).observe(c);
  })();

  /* terminal do ADVPL AI */
  (() => {
    const out = $('#termOut'); if (!out) return;
    const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
    const prompt = out.dataset.prompt + '\n\n', comment = '// ' + out.dataset.comment + '\n';
    const script = [
      ['p', '› '], ['t', prompt], ['c', comment],
      ['k', '#Include '], ['s', '"Protheus.ch"\n\n'],
      ['k', 'User Function '], ['t', 'MT410TOK()\n'],
      ['t', '    '], ['k', 'Local '], ['t', 'lRet  := .T.\n'],
      ['t', '    '], ['k', 'Local '], ['t', 'cCli  := M->C5_CLIENTE\n'],
      ['t', '    '], ['k', 'Local '], ['t', 'cLoja := M->C5_LOJACLI\n\n'],
      ['t', '    SA1->(DbSetOrder(1))\n'],
      ['t', '    '], ['k', 'If '], ['t', 'SA1->(MsSeek(xFilial('], ['s', '"SA1"'], ['t', ') + cCli + cLoja))\n'],
      ['t', '        '], ['k', 'If '], ['t', '!Empty(SA1->A1_VENCLC) .And. SA1->A1_VENCLC < dDataBase\n'],
      ['t', '            Help(, , '], ['s', '"Crédito"'], ['t', ', , '], ['s', '"Limite de crédito vencido."'], ['t', ', 1, 0)\n'],
      ['t', '            lRet := .F.\n'],
      ['t', '        '], ['k', 'EndIf\n'], ['t', '    '], ['k', 'EndIf\n\n'],
      ['k', 'Return '], ['t', 'lRet\n']
    ];
    const part = (k, s) => k === 't' ? esc(s) : `<span class="${k}">${esc(s)}</span>`;
    if (reduce) { out.innerHTML = script.map(([k, s]) => part(k, s)).join(''); return; }
    let running = false, inView = false;
    const run = () => {
      running = true;
      let si = 0, ci = 0, html = '';
      const tick = () => {
        if (si >= script.length) { out.innerHTML = html + '<span class="caret"></span>'; setTimeout(() => { running = false; check(); }, 6000); return; }
        const [k, s] = script[si], slow = si < 2, step = slow ? 1 : 3;
        html += part(k, s.slice(ci, ci + step)); ci += step;
        out.innerHTML = html + '<span class="caret"></span>';
        if (ci >= s.length) { si++; ci = 0; }
        setTimeout(tick, slow ? 20 : (si === 2 && ci === 0 ? 600 : 14));
      };
      tick();
    };
    const check = () => { if (inView && !running) run(); };
    new IntersectionObserver(([e]) => { inView = e.isIntersecting; check(); }, { threshold: .3 }).observe(out);
  })();
})();
