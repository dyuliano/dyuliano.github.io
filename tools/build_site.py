"""Gera as quatro páginas do site a partir de um único conteúdo.

    python3 tools/build_site.py

Saídas:
    index.html        Executivo, português (padrão)
    en/index.html     Executivo, inglês
    v2/index.html     Neo brutalista, português
    v2/en/index.html  Neo brutalista, inglês

Para mudar um texto, edite o dicionário T abaixo (as duas línguas) e rode o script.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://dyuliano.github.io/'

FONTS = {
    'exec': 'https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap',
    'neo': 'https://fonts.googleapis.com/css2?family=Epilogue:wght@700;800;900&family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap',
}

ICONS = {
    'strategy': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
    'people': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.5 3.4-5.5 6.5-5.5s5.7 2 6.5 5.5"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M18 14.7c1.9.7 3.1 2.5 3.5 5.3"/></svg>',
    'ops': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12h4l3-8 4 16 3-8h4"/></svg>',
    'ai': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 10h4v4h-4z"/></svg>',
    'download': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12m0 0-5-5m5 5 5-5M5 21h14"/></svg>',
    'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14m0 0-6-6m6 6 6-6"/></svg>',
}

T = {
'pt': {
    'html_lang': 'pt-BR', 'og_locale': 'pt_BR',
    'title': 'Dyuliano Cecilio · Liderança em Tecnologia',
    'desc': 'Dyuliano Cecilio: liderança em tecnologia, operações Cloud, ERP TOTVS Protheus e IA aplicada. 18 anos de carreira em tecnologia, com foco em sistemas e no desenvolvimento de times.',
    'og_desc': '18 anos de carreira em tecnologia: liderança de times, operações Cloud, ERP TOTVS Protheus e IA aplicada.',
    'og_img': 'assets/og.jpg', 'cv': 'assets/Dyuliano-Cecilio-Curriculo.pdf',
    'intro_cap': 'Dyuliano Cecilio · carreira em tecnologia',
    'nav_label': 'Seções', 'home': 'Início', 'role_short': 'Liderança em tecnologia',
    'menu': [('resumo', 'Resumo'), ('impacto', 'Impacto'), ('trajetoria', 'Trajetória'), ('projetos', 'Projetos'), ('formacao', 'Formação'), ('curriculo', 'Currículo')],
    'lang_label': 'EN', 'lang_aria': 'English version', 'lang_code': 'en',
    'menu_open': 'Abrir menu', 'menu_close': 'Fechar menu',
    'cv_btn': 'Currículo (PDF)',
    'eyebrow': 'Coordenador de Cloud na TOTVS',
    'h1': ('Dyuliano', 'Cecilio'),
    'hero_title': 'Liderança em tecnologia para operações Cloud, ERP TOTVS Protheus e IA aplicada ao negócio.',
    'hero_lede': '18 anos de carreira construída de dentro para fora: do desenvolvimento ADVPL à gestão de áreas de tecnologia, orçamento e ambientes críticos, com reporte direto à diretoria. Hoje coordeno na TOTVS, a maior empresa de software do Brasil, uma operação Cloud que cresceu de 400 para mais de 1.500 clientes com a mesma equipe.',
    'cta1': 'Ver trajetória', 'cta2': 'Baixar currículo',
    'career_lbl': ('2008', '18 anos de carreira', 'hoje'),
    'career_ticks': ['Desenvolvimento', 'Liderança técnica', 'Gestão', 'Escala'],
    'photo_alt': 'Foto de Dyuliano Cecilio',
    'p_name': 'Dyuliano Cecilio de Souza', 'p_role': 'Coordenador de Cloud · TOTVS',
    'facts': [('Atuação', 'Operações Cloud TOTVS Fluig e Agro'), ('Especialidade', 'TOTVS Protheus, gestão de times e IA'), ('Formação', 'MBA Executivo em IA · FAAP'), ('Base', 'Brasil')],
    'links_label': 'Contato e perfis',
    'email_lbl': 'E-mail',
    # resumo
    's_kicker': 'Resumo profissional', 's_h': 'Tecnologia que move o negócio',
    's_p': [
        'Líder de tecnologia com <mark>mais de 15 anos dedicados ao ecossistema TOTVS Protheus</mark>. Conheço o ERP pelos dois lados, negócio e tecnologia: arquitetura, administração, mais de dez migrações de release, integrações e o redesenho de processos financeiros, fiscais, contábeis, de suprimentos, custos, produção e RH.',
        'Minha principal marca é <mark>formar e liderar equipes de analistas e desenvolvedores</mark>. Priorizo demandas por capacidade, desenvolvo pessoas até se tornarem referência técnica e construo times autônomos e de alto desempenho. Já respondi por orçamento de tecnologia, roadmap e reporte direto à diretoria na indústria, no setor automotivo e no software.',
        'Em paralelo, conduzo iniciativas de IA aplicada ao ERP: sou autor do <mark>primeiro modelo público de IA especializado em ADVPL</mark> no Hugging Face e desenvolvo plataformas corporativas próprias de gestão de pessoas, produtividade e IA conversacional para ERP.',
    ],
    'areas_h': 'Áreas de atuação',
    'areas': ['Gestão de equipes de tecnologia', 'Operações Cloud', 'SLA e TMR', 'TOTVS Protheus', 'Orçamento e governança de TI', 'Migração de ERP', 'Integrações e APIs', 'Retenção de clientes', 'IA aplicada e automação', 'Gestão de crise'],
    # indicadores
    'kpi_label': 'Indicadores',
    'kpis': [('1', 'R$ ', 'mi+', 'em custos evitados ao internalizar migração de ERP e infraestrutura'),
             ('18', '&lt;', 'meses', 'de especialista a gerente, com reporte direto à diretoria'),
             ('10', '', '+', 'profissionais desenvolvidos até referência técnica e promovidos'),
             ('150', '', 'mil', 'exemplos no treino do 1º modelo público de IA em ADVPL')],
    # impacto
    'i_kicker': 'Resultado mensurável', 'i_h': 'Escala sem aumentar estrutura',
    'i_p': 'Números de operações reais, construídos com equipes que cresceram em autonomia e capacidade, não em tamanho.',
    'big_aria': 'De 400 para mais de 1.500 clientes', 'big_arr': '→',
    'big_cap': 'clientes atendidos pela operação Cloud, com a mesma equipe',
    'i_text': 'Na TOTVS, a base das linhas Fluig e Agro quase quadruplicou sem aumento de time, sustentada por automação, gestão de capacidade e uso de IA no dia a dia de cada analista.',
    'bar_c': 'Clientes', 'bar_t': 'Equipe', 'bar_same': 'mesma',
    'ratio': ('3,75×', 'mais clientes atendidos por pessoa do time'),
    'dots_aria': 'Cada ponto é um cliente: 400 iniciais e mais de 1.100 incorporados, todos atendidos pela mesma equipe no centro',
    'legend': ['Base inicial (400)', 'Clientes incorporados (1.100+)', 'Mesma equipe'],
    # liderança
    'l_kicker': 'Como eu lidero', 'l_h': 'Quatro frentes, em todas as empresas',
    'l_p': 'Da indústria ao software, a mesma forma de trabalhar: decisões guiadas por capacidade, pessoas no centro e tecnologia medida pelo resultado.',
    'pillars': [
        ('strategy', 'Estratégia e governança', 'Roadmap, priorização por capacidade, risco e viabilidade, com reporte direto à diretoria e à gerência executiva.', ['Orçamento de TI', 'Roadmap', 'Segurança da informação']),
        ('people', 'Pessoas e alto desempenho', 'Formação de analistas e desenvolvedores multidisciplinares, planos de carreira e times autônomos.', ['Mentoria', 'OKRs', 'Times híbridos']),
        ('ops', 'Operação e cliente', 'Ambientes críticos com SLA e TMR sob controle, gestão de capacidade e custo e retenção de contas estratégicas.', ['SLA e TMR', 'Churn', 'Gestão de crise']),
        ('ai', 'Inovação e IA aplicada', 'IA na operação, na rotina das equipes e dentro do ERP, com automação como alavanca de escala.', ['LLMs', 'Agentes', 'Automação']),
    ],
    # trajetória
    't_kicker': 'Trajetória', 't_h': 'Mais escopo a cada etapa',
    't_p': 'Indústria, logística, automotivo e software. De sistemas para pessoas, de pessoas para orçamento, de orçamento para operação em escala nacional.',
    'jobs': [
        {'y': '2022', 'to': 'até hoje', 'now': True, 'org': 'TOTVS S/A · maior empresa de software do Brasil', 'role': 'Coordenador de Cloud',
         'ctx': 'Operação Cloud das linhas TOTVS Fluig e TOTVS Agro, reportando à Gerência de Cloud, com responsabilidade sobre time, indicadores, eficiência operacional e experiência do cliente.',
         'b': ['<b>De 400 para mais de 1.500 clientes</b> sem aumento de equipe, com automação e IA incorporadas à rotina do time.',
               'Ambientes críticos com <b>metas de SLA e TMR cumpridas</b> de forma consistente, apoiadas em gestão de risco e prevenção.',
               'Atuação direta em <b>redução de churn</b>: análise de insatisfação, planos de reversão e atendimento dedicado a contas estratégicas.',
               'Estruturação do Cloud para o ERP TOTVS Agro, migrações on-premises para Cloud e entre edges, e transição do PaaS para <b>Docker e Kubernetes</b>.',
               'Gestão de crise com causa raiz e prevenção de recorrência, junto a Governança e Segurança da Informação.']},
        {'y': '2021', 'to': 'a 2022', 'org': 'Cinbal, Grupo Incoflandres · maior empresa de litografia e beneficiamento de aços planos das Américas', 'role': 'Coordenador de Tecnologia e Desenvolvimento',
         'ctx': 'Área de Tecnologia e Desenvolvimento, reportando à Gerência Executiva.',
         'b': ['<b>Mais de R$ 1 milhão em custos evitados</b>: migração do ERP, parque de servidores, monitoramento, telefonia e disaster recovery feitos pela equipe interna, sem consultoria externa.',
               'Gestão do <b>orçamento de tecnologia</b> e análise de risco e viabilidade para decisões de investimento.',
               'Desenvolvimento da <b>intranet corporativa</b> e de aplicativo para clientes acompanharem informações de produção.',
               'Evolução do Protheus: novos módulos, customizações ADVPL, integradores e sustentação do SQL Server.']},
        {'y': '2019', 'to': 'a 2021', 'org': 'BMB Mode Center e BMB Tech · ecossistema MAN / Volkswagen Caminhões e Ônibus', 'role': 'Gerente de Tecnologia e Inovação',
         'ladder': ['Especialista Sênior', 'Coordenador de TI', 'Head de Tecnologia e Inovação · BMB Tech', 'Gerente de Tecnologia e Inovação'],
         'ctx': 'De especialista a gerente em menos de 18 meses, com reporte direto à diretoria e atuação simultânea na frente de produtos digitais.',
         'b': ['<b>Roadmap e orçamento</b> da área de tecnologia e inovação; gestão por OKRs, Scrum e Kanban.',
               'Migração do ERP e reestruturação de infraestrutura <b>conduzidas pela equipe interna</b>, sem consultoria externa.',
               '<b>Monte Sua Solução</b>: configurador de caminhões integrado ao Protheus, e <b>ROTA</b>: portal para o cliente acompanhar o pedido da solicitação ao faturamento.',
               'Plataforma web e mobile de <b>indicadores de produção, faturamento e despesas</b> integrada ao ERP, com dashboards para a diretoria.']},
        {'y': '2016', 'to': 'a 2019', 'org': 'Fundação CSN', 'role': 'Analista de Sistemas Sênior',
         'ctx': 'Primeira posição de liderança: responsável pela área de sistemas e desenvolvimento, com condução técnica do time e priorização das demandas.',
         'b': ['Sustentação do Protheus em financeiro, fiscal, suprimentos, produção e RH; migração do <b>Protheus 11 para 12</b> e do <b>SQL Server 2000 para 2016</b>.',
               'Desenvolvimento do <b>integrador Protheus x TOTVS RM</b> e do <b>portal do aluno integrado ao RM</b>.',
               'Implantação do TOTVS RM Educacional e da folha ADP; <b>Portal do Fornecedor</b> integrado ao ERP.']},
        {'y': '2014', 'to': 'a 2016', 'org': 'Grupo Toniato · logística', 'role': 'Analista de Desenvolvimento',
         'b': ['Implantação do <b>TOTVS Logix</b> nas operações de WMS e TMS.',
               'Integrações com o Protheus em C#, Razor, JavaScript e SQL, conectando operação logística e backoffice.']},
        {'y': '2011', 'to': 'a 2014', 'org': 'ORMEC Engenharia', 'role': 'Assistente de TI',
         'b': ['Implantação, suporte e customizações ADVPL do <b>Microsiga Protheus</b>; migração do Protheus 10 para 11.',
               'Bancos de dados SQL Server e MySQL, redes e infraestrutura.']},
        {'y': '2008', 'to': 'a 2011', 'org': 'CSN · Prepara', 'role': 'Primeiros passos',
         'b': ['Estágio em programação e controle da produção na <b>Companhia Siderúrgica Nacional</b> (2008).',
               'Instrutor de tecnologia na Prepara Cursos Profissionalizantes (2010–2011).']},
    ],
    # projetos
    'p_kicker': 'Projetos', 'p_h': 'Entregas de destaque',
    'p_p': 'Sistemas que mudaram a forma como as empresas operam, sempre integrados ao ERP e construídos com equipe interna.',
    'projects': [
        ('BMB Mode Center', '2019–2021', 'Monte Sua Solução', 'Configurador web em que o cliente monta o próprio caminhão. Integrado ao Protheus: respeita as regras de estrutura da SG1 e entra no módulo de vendas como pedido de cotação.', ('https://www.modecenter.com.br/solucao', 'Ver ao vivo')),
        ('BMB Mode Center', '2020–2021', 'ROTA', 'Portal do cliente para acompanhar o pedido em tempo real, da solicitação à produção e ao faturamento.', None),
        ('BMB Mode Center', '2020–2021', 'Planejamento orçamentário', 'Orçado e realizado por centro de custo em dashboard, com dados alimentando modelos de machine learning.', None),
        ('BMB Mode Center', '2019–2021', 'Compras, estoque e PCP', 'Controle de alçada por valor e orçamento, estoque com lote e endereçamento e reformulação do PCP.', None),
        ('Intranet corporativa', '', 'Hello', 'Intranet integrada ao Protheus, com indicadores de gestão (KPIs) e workflow de aprovações.', None),
        ('Cinbal', '2021–2022', 'Intranet e app de produção', 'Intranet corporativa e aplicativo para o cliente acompanhar informações de produção.', None),
        ('Fundação CSN', '2016–2019', 'Integrador Protheus x RM', 'Integração entre o Protheus e o TOTVS RM, sincronizando cadastros e processos entre os dois sistemas.', None),
        ('Fundação CSN', '2016–2019', 'Portal do aluno', 'Portal do aluno integrado ao TOTVS RM Educacional.', None),
        ('Fundação CSN', '2016–2019', 'Portal do Fornecedor', 'Portal do Fornecedor integrado ao Protheus.', None),
        ('Várias empresas', '2013–2018', 'Migrações de plataforma', 'Mais de dez migrações de release, entre elas Protheus 10 para 11 e 11 para 12, e SQL Server 2000 para 2016.', None),
    ],
    'prod_h': 'Plataformas próprias',
    'prod_p': 'Produtos que desenvolvo para o mercado corporativo, com foco em gestão, pessoas e IA aplicada ao ERP.',
    'products': [
        ('SinergIA', 'Gestão do trabalho', 'Plataforma corporativa modular que conecta gestão do trabalho, pessoas, conhecimento e IA, com módulo de tempo e produtividade.'),
        ('Pulse', 'SaaS de RH', 'Jornada do colaborador em uma plataforma B2B: recrutamento, admissão digital, ERP e eSocial, onboarding, ponto, performance, PDI e 9Box.'),
        ('MarIA', 'IA para ERP', 'IA conversacional para ERPs: perguntas em linguagem natural sobre estoque, financeiro, compras, faturamento e RH, com respostas auditáveis.'),
        ('IA-ERP Estoque', 'Protheus + IA', 'Especialista de estoque com IA conectado ao Protheus: confere saldos, audita processos e aponta fraudes em linguagem de negócio.'),
        ('ADVPL AI', 'Hugging Face', 'Primeiro modelo público de IA especializado em ADVPL e TLPP, treinado com mais de 150 mil exemplos e executável localmente.'),
        ('Apps executivos', 'App Store e Google Play', 'Dashboards móveis de financeiro e vendas e registro de ponto por geolocalização, publicados nas lojas.'),
    ],
    # IA
    'a_kicker': 'IA aplicada', 'a_h': 'IA dentro do ERP, não ao lado dele',
    'a_p': ['Levo inteligência artificial para onde ela gera ganho real: na operação, na rotina das equipes e dentro do TOTVS Protheus.',
            'O ADVPL AI é o primeiro modelo público especializado na linguagem do Protheus, treinado com mais de 150 mil exemplos de desenvolvimento, banco de dados e regras de negócio. Roda localmente e é aberto à comunidade.'],
    'a_link': 'Ver no Hugging Face',
    'term_aria': 'Exemplo do modelo ADVPL AI gerando um ponto de entrada em ADVPL',
    'term_prompt': 'Crie um ponto de entrada que bloqueie o pedido de venda quando o cliente estiver com crédito vencido.',
    'term_comment': 'Ponto de entrada MT410TOK: validação na gravação do pedido',
    # formação
    'f_kicker': 'Formação', 'f_h': 'Formação acadêmica e certificações',
    'f_p': 'Base técnica em engenharia e sistemas, com especializações em software, dados e, agora, IA aplicada a negócios.',
    'deg_h': 'Acadêmica',
    'degrees': [
        ('2026–2027', 'MBA Executivo em Inteligência Artificial Aplicada a Negócios', 'FAAP · Fundação Armando Alvares Penteado', 'IA generativa e LLMs, machine learning, estratégia e governança de IA, automação inteligente e liderança em ambientes digitais.', 'Em andamento', True),
        ('2020–2021', 'Pós-graduação em Engenharia de Software', 'Universidade Anhanguera', 'Arquitetura, desenvolvimento, qualidade e gestão do ciclo de vida de software.', '', False),
        ('2016–2019', 'Bacharelado em Sistemas de Informação', 'UGB · Centro Universitário Geraldo Di Biase', 'Desenvolvimento de software, bancos de dados e gestão de tecnologia.', '', False),
        ('2013–2016', 'Engenharia de Controle e Automação', 'UBM · Centro Universitário de Barra Mansa', 'Automação, sistemas de controle e integração entre tecnologia e processos industriais.', '', False),
        ('2007–2009', 'Técnico em Mecatrônica', 'ICT', 'Mecânica, eletrônica, automação e manutenção de sistemas.', '', False),
    ],
    'cert_groups': [
        ('Extensão', [('Business Intelligence', 'FIAP · 2021'), ('BI e Business Analytics com Data Science', 'PUC-RS · 2020')]),
        ('Liderança', [('Programa Fora da Curva', 'Fundação Dom Cabral · 2021')]),
        ('Certificações', [('TOTVS Fluig, Plataforma e Negócio', 'TOTVS · 2024'), ('Programação ADVPL', '2016'), ('Folha de Pagamento e Gestão de Funcionários', 'Universidade ADP · 2018'), ('React, Flutter, Vue.js e Front-End', 'Alura · 2020'), ('ASP.NET Razor', 'Alura')]),
    ],
    'cos_label': 'Empresas',
    'cos': ['TOTVS', 'Cinbal · Grupo Incoflandres', 'BMB Mode Center', 'BMB Tech', 'Fundação CSN', 'Grupo Toniato', 'ORMEC Engenharia', 'CSN'],
    # rodapé
    'foot_role': 'Liderança em tecnologia, operações Cloud, ERP e IA aplicada. Brasil.',
    'foot_nav': 'Contato',
    'cv_link': 'Currículo em PDF',
    'alt_theme': {'exec': 'Ver visual alternativo', 'neo': 'Ver visual executivo'},
    'top': 'Voltar ao topo',
    'dl_done': 'Download iniciado',
    'mba_lbl': '{p}% do curso concluído · término em ago. 2027',
    'cv_kicker': 'Currículo', 'cv_h': 'Currículo pronto para download',
    'cv_lead': 'Duas páginas com o mesmo conteúdo deste site, em estrutura limpa para recrutadores, sistemas de recrutamento (ATS) e ferramentas de IA.',
    'cv_points': ['Texto real e pesquisável, sem imagens no lugar do conteúdo', 'Seções padrão: perfil, competências, experiência e formação', 'Versões em português e inglês, mais uma versão em texto puro para IA'],
    'cv_main': 'Baixar PDF', 'cv_other': 'English PDF', 'cv_other_href': 'assets/Dyuliano-Cecilio-Resume.pdf',
    'cv_md': 'Versão em texto (.md)', 'cv_md_href': 'curriculo.md', 'cv_thumb': 'assets/cv-pt.jpg', 'cv_thumb_back': 'assets/cv-pt-2.jpg',
    'cv_thumb_alt': 'Prévia da primeira página do currículo em PDF',
    'fab': 'Baixar currículo',
},
}

T['en'] = {
    'html_lang': 'en', 'og_locale': 'en_US',
    'title': 'Dyuliano Cecilio · Technology Leadership',
    'desc': 'Dyuliano Cecilio: technology leadership, Cloud operations, TOTVS Protheus ERP and applied AI. 18 years in technology, focused on systems and on building teams.',
    'og_desc': '18 years in technology: team leadership, Cloud operations, TOTVS Protheus ERP and applied AI.',
    'og_img': 'assets/og-en.jpg', 'cv': 'assets/Dyuliano-Cecilio-Resume.pdf',
    'intro_cap': 'Dyuliano Cecilio · a career in technology',
    'nav_label': 'Sections', 'home': 'Home', 'role_short': 'Technology leadership',
    'menu': [('resumo', 'Summary'), ('impacto', 'Impact'), ('trajetoria', 'Career'), ('projetos', 'Projects'), ('formacao', 'Education'), ('curriculo', 'Résumé')],
    'lang_label': 'PT', 'lang_aria': 'Versão em português', 'lang_code': 'pt-BR',
    'menu_open': 'Open menu', 'menu_close': 'Close menu',
    'cv_btn': 'Résumé (PDF)',
    'eyebrow': 'Cloud Operations Coordinator at TOTVS',
    'h1': ('Dyuliano', 'Cecilio'),
    'hero_title': 'Technology leadership for Cloud operations, TOTVS Protheus ERP and AI applied to the business.',
    'hero_lede': 'An 18-year career built from the inside out: from ADVPL development to running technology departments, budgets and critical environments, reporting directly to the board. Today, at TOTVS, Brazil\'s largest software company, I run a Cloud operation that grew from 400 to more than 1,500 customers with the same team.',
    'cta1': 'View career', 'cta2': 'Download résumé',
    'career_lbl': ('2008', '18 years in technology', 'today'),
    'career_ticks': ['Development', 'Technical lead', 'Management', 'Scale'],
    'photo_alt': 'Photo of Dyuliano Cecilio',
    'p_name': 'Dyuliano Cecilio de Souza', 'p_role': 'Cloud Operations Coordinator · TOTVS',
    'facts': [('Current', 'TOTVS Fluig and Agro Cloud operations'), ('Expertise', 'TOTVS Protheus, team leadership and AI'), ('Education', 'Executive MBA in AI · FAAP'), ('Based in', 'Brazil')],
    'links_label': 'Contact and profiles',
    'email_lbl': 'Email',
    's_kicker': 'Professional summary', 's_h': 'Technology that moves the business',
    's_p': [
        'Technology leader with <mark>more than 15 years dedicated to the TOTVS Protheus ecosystem</mark>, Latin America\'s leading ERP. I know it from both sides, business and technology: architecture, administration, more than ten release migrations, integrations and the redesign of finance, tax, accounting, procurement, costing, manufacturing and HR processes.',
        'My hallmark is <mark>developing and leading teams of analysts and engineers</mark>. I prioritize by capacity, grow people into technical leads and build autonomous, high-performing teams. I have owned technology budgets and roadmaps and reported directly to the board in manufacturing, automotive and software.',
        'Alongside that, I lead applied-AI initiatives for ERP: I created the <mark>first public AI model specialized in ADVPL</mark> on Hugging Face and build my own corporate platforms for people management, productivity and conversational AI for ERP.',
    ],
    'areas_h': 'Areas of expertise',
    'areas': ['Technology team leadership', 'Cloud operations', 'SLA and MTTR', 'TOTVS Protheus', 'IT budget and governance', 'ERP migration', 'Integrations and APIs', 'Customer retention', 'Applied AI and automation', 'Crisis management'],
    'kpi_label': 'Key figures',
    'kpis': [('1', 'R$ ', 'M+', 'in avoided costs by bringing ERP migration and infrastructure in-house'),
             ('18', '&lt;', 'months', 'from specialist to manager, reporting directly to the board'),
             ('10', '', '+', 'professionals developed into technical leads and promoted'),
             ('150', '', 'k', 'training examples behind the first public AI model in ADVPL')],
    'i_kicker': 'Measurable results', 'i_h': 'Scale without adding structure',
    'i_p': 'Numbers from real operations, built with teams that grew in autonomy and capability, not in size.',
    'big_aria': 'From 400 to more than 1,500 customers', 'big_arr': '→',
    'big_cap': 'customers served by the Cloud operation, with the same team',
    'i_text': 'At TOTVS, the Fluig and Agro customer base nearly quadrupled with no added headcount, sustained by automation, capacity management and everyday use of AI by every analyst.',
    'bar_c': 'Customers', 'bar_t': 'Team', 'bar_same': 'same',
    'ratio': ('3.75×', 'more customers served per team member'),
    'dots_aria': 'Each dot is a customer: the first 400 and more than 1,100 added, all served by the same team at the center',
    'legend': ['Initial base (400)', 'Customers added (1,100+)', 'Same team'],
    'l_kicker': 'How I lead', 'l_h': 'Four fronts, in every company',
    'l_p': 'From manufacturing to software, the same way of working: decisions driven by capacity, people at the center and technology measured by results.',
    'pillars': [
        ('strategy', 'Strategy and governance', 'Roadmap, capacity-based prioritization, risk and feasibility, reporting directly to the board and executive management.', ['IT budget', 'Roadmap', 'Information security']),
        ('people', 'People and high performance', 'Developing multidisciplinary analysts and engineers, career plans and autonomous teams.', ['Mentoring', 'OKRs', 'Hybrid teams']),
        ('ops', 'Operations and customers', 'Critical environments with SLA and MTTR under control, capacity and cost management and strategic account retention.', ['SLA and MTTR', 'Churn', 'Crisis management']),
        ('ai', 'Innovation and applied AI', 'AI in operations, in the team\'s routine and inside the ERP, with automation as the lever for scale.', ['LLMs', 'Agents', 'Automation']),
    ],
    't_kicker': 'Career', 't_h': 'More scope at every step',
    't_p': 'Manufacturing, logistics, automotive and software. From systems to people, from people to budget, from budget to operations at national scale.',
    'jobs': [
        {'y': '2022', 'to': 'to present', 'now': True, 'org': 'TOTVS S/A · Brazil\'s largest software company', 'role': 'Cloud Operations Coordinator',
         'ctx': 'Cloud operation for the TOTVS Fluig and TOTVS Agro product lines, reporting to Cloud management, accountable for team, KPIs, operational efficiency and customer experience.',
         'b': ['<b>From 400 to more than 1,500 customers</b> with no added headcount, with automation and AI built into the team\'s routine.',
               'Critical environments <b>consistently meeting SLA and MTTR targets</b>, backed by risk management and prevention.',
               'Hands-on <b>churn reduction</b>: dissatisfaction analysis, win-back plans and dedicated service for strategic accounts.',
               'Built the Cloud offering for the TOTVS Agro ERP, on-premises to Cloud and cross-edge migrations, and moved PaaS to <b>Docker and Kubernetes</b>.',
               'Crisis management with root cause analysis and recurrence prevention, together with Governance and Information Security.']},
        {'y': '2021', 'to': 'to 2022', 'org': 'Cinbal, Incoflandres Group · the Americas\' largest flat-steel lithography and processing company', 'role': 'Technology and Development Coordinator',
         'ctx': 'Technology and Development department, reporting to executive management.',
         'b': ['<b>More than R$ 1 million in avoided costs</b>: ERP migration, server fleet, monitoring, telephony and disaster recovery delivered by the in-house team, with no outside consultancy.',
               'Managed the <b>technology budget</b> and ran risk and feasibility analysis for investment decisions.',
               'Built the <b>corporate intranet</b> and an app for customers to follow production information.',
               'Evolved Protheus: new modules, ADVPL customizations, integrations and SQL Server operations.']},
        {'y': '2019', 'to': 'to 2021', 'org': 'BMB Mode Center and BMB Tech · MAN / Volkswagen Trucks and Buses ecosystem', 'role': 'Technology and Innovation Manager',
         'ladder': ['Senior Specialist', 'IT Coordinator', 'Head of Technology and Innovation · BMB Tech', 'Technology and Innovation Manager'],
         'ctx': 'From specialist to manager in under 18 months, reporting directly to the board while also leading the digital products front.',
         'b': ['<b>Roadmap and budget</b> for technology and innovation; managed with OKRs, Scrum and Kanban.',
               'ERP migration and infrastructure overhaul <b>delivered by the in-house team</b>, with no outside consultancy.',
               '<b>Monte Sua Solução</b>: a truck configurator integrated with Protheus, and <b>ROTA</b>: a portal for customers to track their order from request to invoicing.',
               'Web and mobile platform for <b>production, billing and expense KPIs</b> integrated with the ERP, with dashboards for the board.']},
        {'y': '2016', 'to': 'to 2019', 'org': 'Fundação CSN', 'role': 'Senior Systems Analyst',
         'ctx': 'First leadership role: responsible for the systems and development area, leading the team technically and prioritizing demand.',
         'b': ['Ran Protheus across finance, tax, procurement, manufacturing and HR; migrated <b>Protheus 11 to 12</b> and <b>SQL Server 2000 to 2016</b>.',
               'Built the <b>Protheus x TOTVS RM integrator</b> and the <b>student portal integrated with RM</b>.',
               'Implemented TOTVS RM Educational and ADP payroll; <b>Supplier Portal</b> integrated with the ERP.']},
        {'y': '2014', 'to': 'to 2016', 'org': 'Grupo Toniato · logistics', 'role': 'Development Analyst',
         'b': ['Implemented <b>TOTVS Logix</b> for WMS and TMS operations.',
               'Protheus integrations in C#, Razor, JavaScript and SQL, connecting logistics operations and back office.']},
        {'y': '2011', 'to': 'to 2014', 'org': 'ORMEC Engenharia', 'role': 'IT Assistant',
         'b': ['<b>Microsiga Protheus</b> implementation, support and ADVPL customizations; migration from Protheus 10 to 11.',
               'SQL Server and MySQL databases, networks and infrastructure.']},
        {'y': '2008', 'to': 'to 2011', 'org': 'CSN · Prepara', 'role': 'First steps',
         'b': ['Production planning and control intern at <b>Companhia Siderúrgica Nacional</b>, Brazil\'s steel giant (2008).',
               'Technology instructor at Prepara vocational school (2010–2011).']},
    ],
    'p_kicker': 'Projects', 'p_h': 'Selected deliveries',
    'p_p': 'Systems that changed how companies operate, always integrated with the ERP and built with in-house teams.',
    'projects': [
        ('BMB Mode Center', '2019–2021', 'Monte Sua Solução', 'Web configurator where customers build their own truck. Integrated with Protheus: it enforces the SG1 bill-of-materials rules and lands in the sales module as a quotation request.', ('https://www.modecenter.com.br/solucao', 'See it live')),
        ('BMB Mode Center', '2020–2021', 'ROTA', 'Customer portal to track each order in real time, from request through production to invoicing.', None),
        ('BMB Mode Center', '2020–2021', 'Budget planning', 'Budget versus actuals by cost center in a dashboard, with the data feeding machine learning models.', None),
        ('BMB Mode Center', '2019–2021', 'Procurement, inventory and PP&amp;C', 'Purchase approval by value and budget, lot and location inventory control and a production planning redesign.', None),
        ('Corporate intranet', '', 'Hello', 'Intranet integrated with Protheus, with management KPIs and approval workflows.', None),
        ('Cinbal', '2021–2022', 'Intranet and production app', 'Corporate intranet and an app for customers to follow production information.', None),
        ('Fundação CSN', '2016–2019', 'Protheus x RM integrator', 'Integration between Protheus and TOTVS RM, synchronizing records and processes across both systems.', None),
        ('Fundação CSN', '2016–2019', 'Student portal', 'Student portal integrated with TOTVS RM Educational.', None),
        ('Fundação CSN', '2016–2019', 'Supplier Portal', 'Supplier portal integrated with Protheus.', None),
        ('Several companies', '2013–2018', 'Platform migrations', 'More than ten release migrations, including Protheus 10 to 11 and 11 to 12, and SQL Server 2000 to 2016.', None),
    ],
    'prod_h': 'Own platforms',
    'prod_p': 'Products I build for the corporate market, focused on management, people and AI applied to ERP.',
    'products': [
        ('SinergIA', 'Work management', 'Modular corporate platform connecting work management, people, knowledge and AI, with a time and productivity module.'),
        ('Pulse', 'HR SaaS', 'The whole employee journey in one B2B platform: recruiting, digital onboarding paperwork, ERP and eSocial, onboarding, time tracking, performance, IDP and 9-box.'),
        ('MarIA', 'AI for ERP', 'Conversational AI for ERPs: natural-language questions about inventory, finance, procurement, billing and HR, with auditable answers.'),
        ('IA-ERP Inventory', 'Protheus + AI', 'An AI inventory specialist connected to Protheus: checks balances, audits processes and flags fraud in business language.'),
        ('ADVPL AI', 'Hugging Face', 'The first public AI model specialized in ADVPL and TLPP, trained on more than 150,000 examples and runnable locally.'),
        ('Executive apps', 'App Store and Google Play', 'Mobile finance and sales dashboards and geolocated time tracking, published on the stores.'),
    ],
    'a_kicker': 'Applied AI', 'a_h': 'AI inside the ERP, not next to it',
    'a_p': ['I bring artificial intelligence where it creates real gains: in operations, in the team\'s routine and inside TOTVS Protheus.',
            'ADVPL AI is the first public model specialized in the Protheus programming language, trained on more than 150,000 examples of development, database and business rules. It runs locally and is open to the community.'],
    'a_link': 'View on Hugging Face',
    'term_aria': 'Example of the ADVPL AI model generating an ADVPL entry point',
    'term_prompt': 'Write an entry point that blocks the sales order when the customer\'s credit limit has expired.',
    'term_comment': 'MT410TOK entry point: validation when the order is saved',
    'f_kicker': 'Education', 'f_h': 'Education and certifications',
    'f_p': 'A technical foundation in engineering and information systems, with specializations in software, data and now AI applied to business.',
    'deg_h': 'Academic',
    'degrees': [
        ('2026–2027', 'Executive MBA, Artificial Intelligence Applied to Business', 'FAAP · Fundação Armando Alvares Penteado', 'Generative AI and LLMs, machine learning, AI strategy and governance, intelligent automation and leadership in digital environments.', 'In progress', True),
        ('2020–2021', 'Postgraduate degree, Software Engineering', 'Universidade Anhanguera', 'Software architecture, development, quality and lifecycle management.', '', False),
        ('2016–2019', 'Bachelor\'s degree, Information Systems', 'UGB · Centro Universitário Geraldo Di Biase', 'Software development, databases and technology management.', '', False),
        ('2013–2016', 'Control and Automation Engineering', 'UBM · Centro Universitário de Barra Mansa', 'Automation, control systems and the integration of technology with industrial processes.', '', False),
        ('2007–2009', 'Mechatronics technician', 'ICT', 'Mechanics, electronics, automation and systems maintenance.', '', False),
    ],
    'cert_groups': [
        ('Extension programs', [('Business Intelligence', 'FIAP · 2021'), ('BI and Business Analytics with Data Science', 'PUC-RS · 2020')]),
        ('Leadership', [('Fora da Curva program', 'Fundação Dom Cabral · 2021')]),
        ('Certifications', [('TOTVS Fluig, Platform and Business', 'TOTVS · 2024'), ('ADVPL Programming', '2016'), ('Payroll and Employee Management', 'ADP University · 2018'), ('React, Flutter, Vue.js and Front-End', 'Alura · 2020'), ('ASP.NET Razor', 'Alura')]),
    ],
    'cos_label': 'Companies',
    'cos': ['TOTVS', 'Cinbal · Incoflandres Group', 'BMB Mode Center', 'BMB Tech', 'Fundação CSN', 'Grupo Toniato', 'ORMEC Engenharia', 'CSN'],
    'foot_role': 'Technology leadership, Cloud operations, ERP and applied AI. Brazil.',
    'foot_nav': 'Contact',
    'cv_link': 'Résumé (PDF)',
    'alt_theme': {'exec': 'See alternative design', 'neo': 'See executive design'},
    'top': 'Back to top',
    'dl_done': 'Download started',
    'mba_lbl': '{p}% of the program complete · ends Aug 2027',
    'cv_kicker': 'Résumé', 'cv_h': 'Résumé ready to download',
    'cv_lead': 'Two pages with the same content as this site, in a clean structure for recruiters, applicant tracking systems (ATS) and AI tools.',
    'cv_points': ['Real, searchable text, with no images standing in for content', 'Standard sections: profile, competencies, experience and education', 'English and Portuguese versions, plus a plain-text version for AI'],
    'cv_main': 'Download PDF', 'cv_other': 'PDF em português', 'cv_other_href': 'assets/Dyuliano-Cecilio-Curriculo.pdf',
    'cv_md': 'Plain-text version (.md)', 'cv_md_href': 'en/resume.md', 'cv_thumb': 'assets/cv-en.jpg', 'cv_thumb_back': 'assets/cv-en-2.jpg',
    'cv_thumb_alt': 'Preview of the first page of the PDF résumé',
    'fab': 'Download résumé',
}

PAGES = [
    # (saída, língua, tema, raiz, link do idioma, link do outro visual, url canônica)
    ('index.html', 'pt', 'exec', '', 'en/', 'v2/', SITE),
    ('en/index.html', 'en', 'exec', '../', '../', '../v2/en/', SITE + 'en/'),
    ('v2/index.html', 'pt', 'neo', '../', 'en/', '../', SITE),
    ('v2/en/index.html', 'en', 'neo', '../../', '../', '../../en/', SITE + 'en/'),
]

LINKS = [('LinkedIn', 'https://www.linkedin.com/in/dyuliano/'), ('GitHub', 'https://github.com/dyuliano'), ('Hugging Face', 'https://huggingface.co/dyulianocecilio')]
EMAIL = 'dyulianocecilio@gmail.com'


def dl_btn(t, href, label, cls, icon=True):
    ic = ICONS['download'] if icon else ''
    return f'<a class="btn {cls}" href="{href}" download data-dl>{ic}<span class="lbl"><span class="go">{label}</span><span class="done" aria-hidden="true">{t["dl_done"]}</span></span></a>'


CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'


def page(t, theme, root, lang_href, alt_href, canonical):
    e = html.escape
    menu = '\n'.join(f'      <li><a href="#{i}">{l}</a></li>' for i, l in t['menu'])
    facts = '\n'.join(f'          <div style="--i:{i}"><dt>{k}</dt><dd>{v}</dd></div>' for i, (k, v) in enumerate(t['facts']))
    links = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in LINKS)
    areas = ''.join(f'<li>{a}</li>' for a in t['areas'])
    summary = '\n'.join(f'        <p>{p}</p>' for p in t['s_p'])
    kpis = '\n'.join(
        f'      <div class="kpi" style="--i:{i}"><div class="n"><span data-to="{to}" data-prefix="{pre}">{pre}0</span><small>{suf}</small></div><span class="bar" aria-hidden="true"></span><p>{txt}</p></div>'
        for i, (to, pre, suf, txt) in enumerate(t['kpis']))
    pillars = '\n'.join(
        f'''      <article class="pillar"><div class="ic">{ICONS[ic]}</div><h3>{h}</h3><p>{p}</p><ul>{''.join(f'<li>{x}</li>' for x in tags)}</ul></article>'''
        for ic, h, p, tags in t['pillars'])
    jobs = []
    for j in t['jobs']:
        ladder = ''
        if j.get('ladder'):
            items = j['ladder']
            spans = []
            for i, x in enumerate(items):
                cls_top = ' class="top"' if i == len(items) - 1 else ''
                spans.append(f'<span{cls_top}>{x}</span>')
            ladder = '<div class="ladder">' + ''.join(spans) + '</div>'
        ctx = f'<p class="ctx">{j["ctx"]}</p>' if j.get('ctx') else ''
        bullets = ''.join(f'<li>{b}</li>' for b in j['b'])
        cls = 'job now' if j.get('now') else 'job'
        jobs.append(f'''      <article class="{cls}"><span class="pin" aria-hidden="true"></span><div class="yr">{j["y"]}<small>{j["to"]}</small></div>
        <div class="org">{j["org"]}</div><h3>{j["role"]}</h3>{ladder}{ctx}<ul>{bullets}</ul></article>''')
    jobs = '\n'.join(jobs)
    prows = []
    for co, yrs, name, desc, link in t['projects']:
        a = f' <a href="{link[0]}" target="_blank" rel="noopener">{link[1]}</a>' if link else ''
        when = f'<small>{yrs}</small>' if yrs else ''
        prows.append(f'      <div class="prow"><div class="co">{co}{when}</div><h3>{name}</h3><p>{desc}{a}</p></div>')
    prows = '\n'.join(prows)
    prods = '\n'.join(f'      <article class="prod"><div class="pt"><h3>{n}</h3><span class="badge">{b}</span></div><p>{d}</p></article>' for n, b, d in t['products'])
    a_p = '\n'.join(f'        <p>{p}</p>' for p in t['a_p'])
    degs = []
    for when, name, inst, desc, st, hl in t['degrees']:
        badge = f'<span class="st">{st}</span>' if st else ''
        prog = f'<div class="mba" data-start="2026-08-01" data-end="2027-08-31" data-label="{t["mba_lbl"]}"><div class="tr"><i></i></div><span></span></div>' if hl else ''
        degs.append(f'        <article class="deg{" hl" if hl else ""}"><div class="when">{when}</div><div><h3>{name}{badge}</h3><div class="inst">{inst}</div><p>{desc}</p>{prog}</div></article>')
    degs = '\n'.join(degs)
    certs = ''
    for g, items in t['cert_groups']:
        certs += f'<h3>{g}</h3><dl>' + ''.join(f'<div class="r"><dt>{n}</dt><dd>{w}</dd></div>' for n, w in items) + '</dl>'
    cos = ''.join(f'<li>{c}</li>' for c in t['cos'])
    legend_colors = ['var(--dot-base)', 'var(--dot-new)', 'var(--team)']
    legend = ''.join(f'<span><i style="background:{c};box-shadow:0 0 0 1px var(--ink)"></i>{l}</span>' if i == 2 else f'<span><i style="background:{c}"></i>{l}</span>' for i, (c, l) in enumerate(zip(legend_colors, t['legend'])))
    cl = t['career_lbl']
    ticks = ''.join(f'<span>{x}</span>' for x in t['career_ticks'])
    alt_label = t['alt_theme'][theme]
    other_lang = 'en' if t['html_lang'].startswith('pt') else 'pt-BR'
    alt_lang_url = SITE + ('en/' if other_lang == 'en' else '')
    noindex = '\n<meta name="robots" content="noindex">' if theme == 'neo' else ''

    return f'''<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{e(t['desc'])}">
<meta name="author" content="Dyuliano Cecilio de Souza">{noindex}
<meta property="og:type" content="profile">
<meta property="og:title" content="Dyuliano Cecilio">
<meta property="og:description" content="{e(t['og_desc'])}">
<meta property="og:locale" content="{t['og_locale']}">
<meta property="og:site_name" content="Dyuliano Cecilio">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}{t['og_img']}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="{other_lang}" href="{alt_lang_url}">
<link rel="apple-touch-icon" href="{root}assets/rosto.jpg">
<meta name="theme-color" content="{'#0E1726' if theme == 'exec' else '#FAF9F4'}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%230E1726'/%3E%3Ctext x='50%25' y='56%25' text-anchor='middle' dominant-baseline='middle' font-family='Arial,sans-serif' font-weight='700' font-size='26' fill='%23ffffff'%3EDC%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS[theme]}" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/theme-{theme}.css">
<link rel="stylesheet" href="{root}assets/site.css">
<link rel="stylesheet" href="{root}assets/motion.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Person","name":"Dyuliano Cecilio de Souza","jobTitle":"{t['p_role'].split(' · ')[0]}","worksFor":{{"@type":"Organization","name":"TOTVS"}},"address":{{"@type":"PostalAddress","addressCountry":"BR"}},"url":"{canonical}","sameAs":["https://www.linkedin.com/in/dyuliano/","https://github.com/dyuliano","https://huggingface.co/dyulianocecilio"]}}
</script>
<noscript><style>#intro{{display:none}}body.loading{{overflow:auto}}.reveal{{opacity:1;transform:none}}.career .track i{{width:100%}}</style></noscript>
</head>
<body class="loading">

<div id="intro" data-from="2008" aria-hidden="true">
  <div class="box"><div class="year">2008</div><div class="bar"><i></i></div><div class="cap">{t['intro_cap']}</div></div>
</div>
<div class="progress" id="progress"></div>

<header class="top" id="nav">
  <div class="wrap">
    <a class="brand" href="#inicio" aria-label="{t['home']}"><span class="mark">DC</span><span class="nm"><b>Dyuliano Cecilio</b><small>{t['role_short']}</small></span></a>
    <nav aria-label="{t['nav_label']}">
    <ul class="menu" id="menu">
{menu}
    </ul>
    </nav>
    <div class="tools">
      <a class="lang" href="{lang_href}" hreflang="{t['lang_code']}" lang="{t['lang_code']}" aria-label="{t['lang_aria']}">{t['lang_label']}</a>
      {dl_btn(t, root + t['cv'], t['cv_btn'], 'primary sm')}
      <button class="menu-btn" id="menuBtn" aria-label="{t['menu_open']}" aria-expanded="false" aria-controls="menu" data-open="{t['menu_open']}" data-close="{t['menu_close']}"><i></i><i></i></button>
    </div>
  </div>
</header>

<main>
<section class="hero" id="inicio">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow" data-in style="--i:0"><span class="dot" aria-hidden="true"></span>{t['eyebrow']}</p>
      <h1><span>{t['h1'][0]}</span> <span>{t['h1'][1]}</span></h1>
      <p class="title" data-in style="--i:2">{t['hero_title']}</p>
      <p class="lede" data-in style="--i:3">{t['hero_lede']}</p>
      <div class="actions" data-in style="--i:4">
        <a class="btn primary" href="#trajetoria">{t['cta1']}{ICONS['arrow']}</a>
        {dl_btn(t, root + t['cv'], t['cta2'], 'ghost')}
      </div>
      <div class="career" aria-hidden="true" data-in style="--i:5">
        <div class="lbl"><span>{cl[0]}</span><span>{cl[1]}</span><span>{cl[2]}</span></div>
        <div class="track"><i id="careerFill"></i><span class="rider" id="careerRider"><b>2008</b></span></div>
        <div class="ticks">{ticks}</div>
      </div>
    </div>
    <aside class="profile" data-in style="--i:3" aria-label="{t['links_label']}">
      <div class="head">
        <div class="avatar"><span class="ring" aria-hidden="true"></span><img src="{root}assets/rosto.jpg" alt="{t['photo_alt']}" width="108" height="108"></div>
        <div class="who"><b>{t['p_name']}</b><span>{t['p_role']}</span></div>
      </div>
      <dl class="facts">
{facts}
      </dl>
      <div class="links"><a href="mailto:{EMAIL}">{t['email_lbl']}</a>{links}</div>
    </aside>
  </div>
</section>

<section class="sec" id="resumo">
  <div class="wrap">
    <div class="sec-head reveal"><div><span class="kicker">{t['s_kicker']}</span><h2>{t['s_h']}</h2></div></div>
    <div class="summary">
      <div class="txt reveal">
{summary}
      </div>
      <aside class="areas reveal"><h3>{t['areas_h']}</h3><ul class="tags" data-stagger>{areas}</ul></aside>
    </div>
  </div>
</section>

<section class="kpis" aria-label="{t['kpi_label']}">
  <div class="wrap">
    <div class="kpi-grid">
{kpis}
    </div>
  </div>
</section>

<section class="sec alt" id="impacto">
  <div class="wrap">
    <div class="sec-head reveal"><div><span class="kicker">{t['i_kicker']}</span><h2>{t['i_h']}</h2></div><p>{t['i_p']}</p></div>
    <div class="big reveal" aria-label="{t['big_aria']}"><span class="from">400</span><span class="arr">{t['big_arr']}</span><span class="to" id="scaleTo">400</span><span class="to">+</span></div>
    <p class="big-cap reveal">{t['big_cap']}</p>
    <div class="impact-grid">
      <div class="panel stack reveal">
        <p class="muted">{t['i_text']}</p>
        <div class="bars" aria-hidden="true">
          <div class="bar-row"><span>{t['bar_c']}</span><div class="tr"><i class="base" style="width:26.7%"></i><i class="grow" id="barGrow"></i></div><span class="v" id="barV">400</span></div>
          <div class="bar-row"><span>{t['bar_t']}</span><div class="tr"><i class="team"></i></div><span class="v">{t['bar_same']}</span></div>
        </div>
        <div class="ratio" id="ratio"><b>{t['ratio'][0]}</b><span>{t['ratio'][1]}</span></div>
      </div>
      <div class="panel reveal">
        <canvas id="dots" role="img" aria-label="{t['dots_aria']}"></canvas>
        <div class="legend">{legend}</div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="lideranca">
  <div class="wrap">
    <div class="sec-head reveal"><div><span class="kicker">{t['l_kicker']}</span><h2>{t['l_h']}</h2></div><p>{t['l_p']}</p></div>
    <div class="pillars" data-stagger>
{pillars}
    </div>
  </div>
</section>

<div class="cos" aria-label="{t['cos_label']}"><div class="track"><ul>{cos}</ul><ul aria-hidden="true">{cos}</ul></div></div>

<section class="sec alt" id="trajetoria">
  <div class="wrap">
    <div class="sec-head reveal"><div><span class="kicker">{t['t_kicker']}</span><h2>{t['t_h']}</h2></div><p>{t['t_p']}</p></div>
    <div class="tl" id="tl">
      <div class="rail" aria-hidden="true"><i id="railFill"></i></div>
{jobs}
    </div>
  </div>
</section>

<section class="sec" id="projetos">
  <div class="wrap">
    <div class="sec-head reveal"><div><span class="kicker">{t['p_kicker']}</span><h2>{t['p_h']}</h2></div><p>{t['p_p']}</p></div>
    <div class="plist" data-stagger>
{prows}
    </div>
    <h3 class="sub-h reveal">{t['prod_h']}</h3>
    <p class="sub-p reveal">{t['prod_p']}</p>
    <div class="products" data-stagger>
{prods}
    </div>
  </div>
</section>

<section class="sec alt" id="ia">
  <div class="wrap ai-grid">
    <div class="txt reveal">
      <div><span class="kicker">{t['a_kicker']}</span><h2 style="font-size:clamp(30px,4vw,46px)">{t['a_h']}</h2></div>
{a_p}
      <p><a href="https://huggingface.co/dyulianocecilio" target="_blank" rel="noopener">{t['a_link']}</a></p>
    </div>
    <div class="term reveal" role="img" aria-label="{t['term_aria']}">
      <div class="tb"><i></i><i></i><i></i><span>advpl-ai · local</span></div>
      <pre id="termOut" aria-hidden="true" data-prompt="{e(t['term_prompt'])}" data-comment="{e(t['term_comment'])}"></pre>
    </div>
  </div>
</section>

<section class="sec" id="formacao">
  <div class="wrap">
    <div class="sec-head reveal"><div><span class="kicker">{t['f_kicker']}</span><h2>{t['f_h']}</h2></div><p>{t['f_p']}</p></div>
    <div class="edu-grid">
      <div class="degrees" data-stagger>
{degs}
      </div>
      <aside class="certs reveal">{certs}</aside>
    </div>
  </div>
</section>

<section class="sec alt cv-sec reveal" id="curriculo">
  <div class="wrap">
    <div class="cv-card">
      <div>
        <span class="kicker">{t['cv_kicker']}</span>
        <h2>{t['cv_h']}</h2>
        <p class="lead">{t['cv_lead']}</p>
        <ul class="cv-points">{''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in t['cv_points'])}</ul>
        <div class="cv-actions">
          {dl_btn(t, root + t['cv'], t['cv_main'], 'primary')}
          {dl_btn(t, root + t['cv_other_href'], t['cv_other'], 'ghost')}
          <a class="alt" href="{root}{t['cv_md_href']}">{t['cv_md']}</a>
        </div>
      </div>
      <div class="cv-preview" aria-hidden="true">
        <span class="sheet back"><img src="{root}{t['cv_thumb_back']}" alt="" width="600" height="849" loading="lazy"></span>
        <a class="sheet" href="{root}{t['cv']}" download data-dl tabindex="-1"><img src="{root}{t['cv_thumb']}" alt="{t['cv_thumb_alt']}" width="600" height="849" loading="lazy"></a>
      </div>
    </div>
  </div>
</section>
</main>
{dl_btn(t, root + t['cv'], t['fab'], 'primary fab')}

<footer class="foot" id="contato">
  <div class="wrap">
    <div class="foot-top">
      <div><b>Dyuliano Cecilio</b><p>{t['foot_role']}</p></div>
      <nav aria-label="{t['foot_nav']}"><a href="mailto:{EMAIL}">{EMAIL}</a>{links}<a href="{root}{t['cv']}" download data-dl>{t['cv_link']}</a></nav>
    </div>
    <div class="foot-base"><span>© <span data-year>2026</span> Dyuliano Cecilio de Souza · <a href="{alt_href}">{alt_label}</a></span><a href="#inicio">{t['top']}</a></div>
  </div>
</footer>

<script src="{root}assets/site.js"></script>
</body>
</html>
'''


def plain(x):
    import re
    return html.unescape(re.sub(r'<[^>]+>', '', x))


def markdown(t, lang):
    pt = lang == 'pt'
    L = []
    L.append('# Dyuliano Cecilio de Souza')
    L.append('')
    L.append(plain(t['hero_title']))
    L.append('')
    L.append(f"- {'Cargo atual' if pt else 'Current role'}: {t['p_role']}")
    L.append(f"- {'Localização' if pt else 'Location'}: {'Brasil' if pt else 'Brazil'}")
    L.append(f'- E-mail: {EMAIL}')
    L.append('- LinkedIn: https://www.linkedin.com/in/dyuliano/')
    L.append(f"- Site: {SITE}{'' if pt else 'en/'}")
    L.append('- GitHub: https://github.com/dyuliano')
    L.append('- Hugging Face: https://huggingface.co/dyulianocecilio')
    L.append('')
    L.append(f"## {'Resumo profissional' if pt else 'Professional summary'}")
    L.append('')
    for p_ in t['s_p']:
        L.append(plain(p_))
        L.append('')
    L.append(f"## {'Resultados' if pt else 'Key results'}")
    L.append('')
    L.append(f"- 400 → 1.500+ {plain(t['big_cap'])}" if pt else f"- 400 → 1,500+ {plain(t['big_cap'])}")
    for to, pre, suf, txt in t['kpis']:
        sep = '' if suf == '+' else ' '
        L.append(f'- {plain(pre)}{to}{sep}{suf}: {plain(txt)}')
    L.append('')
    L.append(f"## {'Áreas de atuação' if pt else 'Areas of expertise'}")
    L.append('')
    L.append(', '.join(t['areas']) + '.')
    L.append('')
    L.append(f"## {'Experiência profissional' if pt else 'Professional experience'}")
    L.append('')
    for j in t['jobs']:
        L.append(f"### {j['role']} | {plain(j['org'])}")
        L.append(f"{j['y']} {j['to']}")
        L.append('')
        if j.get('ladder'):
            L.append(('Progressão: ' if pt else 'Progression: ') + ' → '.join(j['ladder']))
            L.append('')
        if j.get('ctx'):
            L.append(plain(j['ctx']))
            L.append('')
        for b in j['b']:
            L.append('- ' + plain(b))
        L.append('')
    L.append(f"## {'Projetos de destaque' if pt else 'Selected projects'}")
    L.append('')
    for co, yrs, name, desc, link in t['projects']:
        extra = f' ({link[0]})' if link else ''
        when = f', {yrs}' if yrs else ''
        L.append(f'- **{plain(name)}** ({co}{when}): {plain(desc)}{extra}')
    L.append('')
    L.append(f"## {plain(t['prod_h'])}")
    L.append('')
    for n, b, d in t['products']:
        L.append(f'- **{n}** ({b}): {plain(d)}')
    L.append('')
    L.append(f"## {'Formação acadêmica' if pt else 'Education'}")
    L.append('')
    for when, name, inst, desc, st, hl in t['degrees']:
        st_ = f' ({st})' if st else ''
        L.append(f'- **{name}**{st_}, {inst}, {when}. {plain(desc)}')
    L.append('')
    for g, items in t['cert_groups']:
        L.append(f'### {g}')
        L.append('')
        for n, w in items:
            L.append(f'- {plain(n)}, {w}')
        L.append('')
    return '\n'.join(L).rstrip() + '\n'


LLMS = """# Dyuliano Cecilio de Souza

> Technology leader in Brazil: Cloud operations at TOTVS, TOTVS Protheus ERP (15+ years), team leadership and applied AI. Author of the first public AI model specialized in ADVPL.

## Résumé
- [Currículo em texto (português)](https://dyuliano.github.io/curriculo.md)
- [Résumé in plain text (English)](https://dyuliano.github.io/en/resume.md)
- [Currículo em PDF](https://dyuliano.github.io/assets/Dyuliano-Cecilio-Curriculo.pdf)
- [Résumé PDF](https://dyuliano.github.io/assets/Dyuliano-Cecilio-Resume.pdf)

## Profiles
- [LinkedIn](https://www.linkedin.com/in/dyuliano/)
- [GitHub](https://github.com/dyuliano)
- [Hugging Face](https://huggingface.co/dyulianocecilio)
"""


def main():
    (ROOT / 'curriculo.md').write_text(markdown(T['pt'], 'pt'), encoding='utf-8')
    (ROOT / 'en').mkdir(exist_ok=True)
    (ROOT / 'en' / 'resume.md').write_text(markdown(T['en'], 'en'), encoding='utf-8')
    (ROOT / 'llms.txt').write_text(LLMS, encoding='utf-8')
    print('ok: curriculo.md, en/resume.md, llms.txt')
    for out, lang, theme, root, lang_href, alt_href, canonical in PAGES:
        dest = ROOT / out
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page(T[lang], theme, root, lang_href, alt_href, canonical), encoding='utf-8')
        print('ok:', out)


if __name__ == '__main__':
    main()
