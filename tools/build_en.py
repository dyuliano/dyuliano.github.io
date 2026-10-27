"""Gera en/index.html a partir de index.html (fonte em português).

Uso: python3 tools/build_en.py
Cada par (pt, en) precisa existir no index.html; se um texto em português
mudar, o script para e aponta qual par precisa ser atualizado.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

PAIRS = [
    # ---- head ----
    ('<html lang="pt-BR">', '<html lang="en">'),
    ('<meta name="description" content="Dyuliano Cecilio — liderança em tecnologia, operações Cloud, ERP TOTVS Protheus e IA aplicada. 18 anos de carreira em tecnologia, com foco em sistemas e no desenvolvimento de times.">',
     '<meta name="description" content="Dyuliano Cecilio: technology leadership, Cloud operations, TOTVS Protheus ERP and applied AI. 18 years in technology, focused on systems and on building teams.">'),
    ('<meta property="og:description" content="18 anos de carreira em tecnologia: liderança de times, operações Cloud, ERP e IA aplicada. Da linha de código à mesa da diretoria.">',
     '<meta property="og:description" content="18 years in technology: team leadership, Cloud operations, ERP and applied AI. From the first line of code to the boardroom.">'),
    ('<meta property="og:locale" content="pt_BR">', '<meta property="og:locale" content="en_US">'),
    ('<meta property="og:url" content="https://dyuliano.github.io/">', '<meta property="og:url" content="https://dyuliano.github.io/en/">'),
    ('content="Dyuliano Cecilio, liderança em tecnologia, operações Cloud, ERP e IA aplicada"', 'content="Dyuliano Cecilio, technology leadership, Cloud operations, ERP and applied AI"'),
    ('<meta property="og:image" content="https://dyuliano.github.io/assets/og.jpg">', '<meta property="og:image" content="https://dyuliano.github.io/assets/og-en.jpg">'),
    ('<link rel="canonical" href="https://dyuliano.github.io/">', '<link rel="canonical" href="https://dyuliano.github.io/en/">'),
    ('<link rel="apple-touch-icon" href="assets/foto.jpg">', '<link rel="apple-touch-icon" href="../assets/foto.jpg">'),
    ('"jobTitle":"Coordenador de Cloud"', '"jobTitle":"Cloud Operations Coordinator"'),
    ('"url":"https://dyuliano.github.io/"', '"url":"https://dyuliano.github.io/en/"'),

    # ---- nav ----
    ('<nav class="top" id="nav" aria-label="Seções">', '<nav class="top" id="nav" aria-label="Sections">'),
    ('aria-label="Início">DC</a>', 'aria-label="Home">DC</a>'),
    ('<li><a href="#impacto">Impacto</a></li>', '<li><a href="#impacto">Impact</a></li>'),
    ('<li><a href="#lideranca">Liderança</a></li>', '<li><a href="#lideranca">Leadership</a></li>'),
    ('<li><a href="#trajetoria">Trajetória</a></li>', '<li><a href="#trajetoria">Career</a></li>'),
    ('<li><a href="#projetos">Projetos</a></li>', '<li><a href="#projetos">Projects</a></li>'),
    ('<li><a href="#ia">IA e inovação</a></li>', '<li><a href="#ia">AI and innovation</a></li>'),
    ('<li><a href="#contato">Contato</a></li>', '<li><a href="#contato">Contact</a></li>'),
    ('<a class="lang" href="en/" hreflang="en" lang="en" aria-label="English version">EN</a>',
     '<a class="lang" href="../" hreflang="pt-BR" lang="pt-BR" aria-label="Versão em português">PT</a>'),
    ('aria-label="Abrir menu" aria-expanded="false"', 'aria-label="Open menu" aria-expanded="false"'),
    ("open ? 'Fechar menu' : 'Abrir menu'", "open ? 'Close menu' : 'Open menu'"),

    # ---- hero ----
    ('Liderança em tecnologia, operações Cloud e ERP, com IA aplicada ao negócio.</p>',
     'Technology leadership across Cloud operations and ERP, with AI applied to the business.</p>'),
    ('18 anos de carreira em tecnologia, com foco em sistemas e no desenvolvimento de times — da primeira linha de código à mesa da diretoria. Hoje na TOTVS, a maior empresa de software do Brasil.',
     '18 years in technology, focused on systems and on building teams — from the first line of code to the boardroom. Currently at TOTVS, Brazil\'s largest software company.'),
    ('href="#trajetoria">Conhecer a trajetória</a>', 'href="#trajetoria">Explore my career</a>'),
    ('href="assets/Dyuliano-Cecilio-Curriculo.pdf" download>\n          <svg', 'href="../assets/Dyuliano-Cecilio-Resume.pdf" download>\n          <svg'),
    ('          Baixar currículo\n', '          Download résumé\n'),
    ('<img src="assets/foto.jpg" alt="Retrato de Dyuliano Cecilio"', '<img src="../assets/foto.jpg" alt="Portrait of Dyuliano Cecilio"'),
    ('<b>15+ anos</b>em sistemas e desenvolvimento de times', '<b>15+ years</b>in systems and team development'),

    # ---- manifesto ----
    ('<section class="manifesto" aria-label="Perfil">', '<section class="manifesto" aria-label="Profile">'),
    ('Construí minha carreira de dentro para fora. Comecei escrevendo código, implantando ERP e resolvendo problemas na operação. Hoje respondo por pessoas, orçamento e ambientes críticos — com a mesma convicção de sempre: tecnologia só importa quando move o negócio.',
     'I built my career from the inside out. I started by writing code, implementing ERP and solving problems on the operations floor. Today I am accountable for people, budget and critical environments — with the same conviction as always: technology only matters when it moves the business.'),
    ('Conheço o TOTVS Protheus pelos dois lados, negócio e tecnologia: arquitetura, migrações e integrações, e o redesenho de processos financeiros, fiscais, de suprimentos, produção e RH. É dessa base que vem a forma como lidero.',
     'I know TOTVS Protheus, Latin America\'s leading ERP, from both sides, business and technology: architecture, migrations and integrations, and the redesign of finance, tax, procurement, manufacturing and HR processes. That foundation shapes the way I lead.'),

    # ---- impact ----
    ('<h2>Resultado mensurável</h2>', '<h2>Measurable results</h2>'),
    ('Números de operações reais, construídos com equipes que cresceram em autonomia e capacidade, não em tamanho.',
     'Numbers from real operations, built with teams that grew in autonomy and capability, not in size.'),
    ('aria-label="De 400 para mais de 1.500 clientes"><span class="from">400</span><span class="arrow">a</span>',
     'aria-label="From 400 to more than 1,500 customers"><span class="from">400</span><span class="arrow">to</span>'),
    ('<h3>Clientes atendidos pela operação Cloud, com a mesma equipe</h3>', '<h3>Customers served by the Cloud operation, with the same team</h3>'),
    ('Na TOTVS, a base das linhas Fluig e Agro quase quadruplicou sem aumento de time — sustentada por automação, gestão de capacidade e uso de IA no dia a dia de cada analista.',
     'At TOTVS, the Fluig and Agro customer base nearly quadrupled with no added headcount — sustained by automation, capacity management and everyday use of AI by every analyst.'),
    ('<div class="bar-row"><span>Clientes</span>', '<div class="bar-row"><span>Customers</span>'),
    ('<div class="bar-row"><span>Equipe</span><div class="track"><i class="team"></i></div><span class="bv">mesma</span></div>',
     '<div class="bar-row"><span>Team</span><div class="track"><i class="team"></i></div><span class="bv">same</span></div>'),
    ('<b>3,75×</b><span>mais clientes atendidos por pessoa do time</span>', '<b>3.75×</b><span>more customers served per team member</span>'),
    ('aria-label="Cada ponto representa um cliente: 400 iniciais e mais de 1.100 incorporados, todos atendidos pela mesma equipe no centro"',
     'aria-label="Each dot is a customer: the first 400 and more than 1,100 added, all served by the same team at the center"'),
    ('</i>Base inicial</span>', '</i>Initial base</span>'),
    ('</i>Clientes incorporados</span>', '</i>Customers added</span>'),
    ('</i>Mesma equipe</span>', '</i>Same team</span>'),
    ('<small>mi+</small></div><p>em custos evitados ao internalizar migração de ERP e projetos de infraestrutura</p>',
     '<small>M+</small></div><p>in avoided costs by bringing ERP migration and infrastructure projects in-house</p>'),
    ('<small>meses</small></div><p>de especialista a gerente, com reporte direto à diretoria</p>',
     '<small>months</small></div><p>from specialist to manager, reporting directly to the board</p>'),
    ('<p>profissionais formados até se tornarem referências técnicas e promovidos</p>',
     '<p>professionals developed into technical leads and promoted</p>'),
    ('<small>mil</small></div><p>exemplos no treino do primeiro modelo público de IA especializado em ADVPL</p>',
     '<small>k</small></div><p>training examples behind the first public AI model specialized in ADVPL</p>'),

    # ---- leadership ----
    ('<h2>Como eu lidero</h2>', '<h2>How I lead</h2>'),
    ('Quatro frentes que se repetem em todas as empresas por onde passei, da indústria ao software.',
     'Four fronts that repeat in every company I have worked for, from manufacturing to software.'),
    ('<span class="pt">Estratégia, orçamento e governança</span>', '<span class="pt">Strategy, budget and governance</span>'),
    ('Defino roadmap, priorizo por capacidade e transformo investimento em tecnologia em decisão de negócio — com análise de risco e viabilidade, e reporte direto à diretoria e à gerência executiva.',
     'I set the roadmap, prioritize by capacity and turn technology spending into business decisions — with risk and feasibility analysis, reporting directly to the board and executive management.'),
    ('<ul><li>Roadmap de tecnologia</li><li>Orçamento de TI</li><li>Risco e viabilidade</li><li>Reporte à diretoria</li><li>Governança e segurança da informação</li></ul>',
     '<ul><li>Technology roadmap</li><li>IT budget</li><li>Risk and feasibility</li><li>Board reporting</li><li>Governance and information security</li></ul>'),
    ('<span class="pt">Pessoas e times de alto desempenho</span>', '<span class="pt">People and high-performing teams</span>'),
    ('Minha principal marca. Formo analistas e desenvolvedores multidisciplinares, construo times autônomos e cuido de carreira de forma concreta: mais de dez profissionais desenvolvidos até virarem referência, com promoções de analista a especialista.',
     'My hallmark. I develop multidisciplinary analysts and engineers, build autonomous teams and take careers seriously: more than ten professionals grown into technical leads, with promotions from analyst to specialist.'),
    ('<ul><li>Mentoria</li><li>Planos de carreira</li><li>Avaliação de desempenho</li><li>OKRs</li><li>Scrum e Kanban</li><li>Times remotos e híbridos</li></ul>',
     '<ul><li>Mentoring</li><li>Career plans</li><li>Performance reviews</li><li>OKRs</li><li>Scrum and Kanban</li><li>Remote and hybrid teams</li></ul>'),
    ('<span class="pt">Operação, eficiência e cliente</span>', '<span class="pt">Operations, efficiency and customers</span>'),
    ('Operações críticas com SLA e tempo médio de resolução sob controle, gestão de capacidade e custo, e atuação direta em retenção: análise de insatisfação, planos de reversão e atendimento dedicado para contas estratégicas.',
     'Critical operations with SLA and mean time to resolution under control, capacity and cost management, and hands-on retention: dissatisfaction analysis, win-back plans and dedicated service for strategic accounts.'),
    ('<ul><li>SLA e TMR</li><li>Gestão de capacidade</li><li>Custo operacional</li><li>Redução de churn</li><li>Gestão de crise e causa raiz</li></ul>',
     '<ul><li>SLA and MTTR</li><li>Capacity management</li><li>Operating cost</li><li>Churn reduction</li><li>Crisis and root cause management</li></ul>'),
    ('<span class="pt">Inovação e IA aplicada</span>', '<span class="pt">Innovation and applied AI</span>'),
    ('Levo IA para onde ela gera ganho real: na operação, na rotina das equipes e dentro do ERP. Do ajuste fino de modelos à adoção pelo time, com automação como alavanca de escala.',
     'I bring AI where it creates real gains: in operations, in the team\'s routine and inside the ERP. From fine-tuning models to team adoption, with automation as the lever for scale.'),
    ('<ul><li>LLMs e fine-tuning</li><li>IA local</li><li>Agentes</li><li>Automação de operações</li><li>Adoção de IA pelas equipes</li></ul>',
     '<ul><li>LLMs and fine-tuning</li><li>Local AI</li><li>Agents</li><li>Operations automation</li><li>AI adoption across teams</li></ul>'),
    ('<span>Cinbal, Grupo Incoflandres</span>', '<span>Cinbal, Incoflandres Group</span>'),

    # ---- career ----
    ('<h2>Trajetória</h2>', '<h2>Career</h2>'),
    ('Indústria, logística, automotivo e software. Em cada etapa, mais escopo: de sistemas para pessoas, de pessoas para orçamento, de orçamento para operação em escala nacional.',
     'Manufacturing, logistics, automotive and software. Each step brought more scope: from systems to people, from people to budget, from budget to operations at national scale.'),
    ('<small>a 2014</small>', '<small>to 2014</small>'),
    ('<small>a 2016</small>', '<small>to 2016</small>'),
    ('<small>a 2019</small>', '<small>to 2019</small>'),
    ('<small>a 2021</small>', '<small>to 2021</small>'),
    ('<small>a 2022</small>', '<small>to 2022</small>'),
    ('<small>até hoje</small>', '<small>to present</small>'),
    ('<h3>Fundamentos</h3>', '<h3>Foundations</h3>'),
    ('<li>Início como estagiário na CSN e passagem como instrutor de tecnologia na Prepara.</li>',
     '<li>Started as an intern at CSN, Brazil\'s steel giant, and taught technology courses at Prepara.</li>'),
    ('<li>Na ORMEC Engenharia, <b>implantação e suporte do TOTVS Protheus</b>: a base técnica e funcional que sustenta toda a carreira.</li>',
     '<li>At ORMEC Engenharia, <b>TOTVS Protheus implementation and support</b>: the technical and functional foundation of my whole career.</li>'),
    ('<p class="org">Grupo Toniato · logística</p>', '<p class="org">Grupo Toniato · logistics</p>'),
    ('<h3>Analista de Desenvolvimento</h3>', '<h3>Development Analyst</h3>'),
    ('<li><b>Implantação do TOTVS Logix</b> nos módulos de WMS e TMS.</li>', '<li><b>Implemented TOTVS Logix</b> WMS and TMS modules.</li>'),
    ('<li>Integrações com o Protheus em C#, Razor e SQL, conectando operação logística e backoffice.</li>',
     '<li>Protheus integrations in C#, Razor and SQL, connecting logistics operations and back office.</li>'),
    ('<h3>Analista de Sistemas Sênior</h3>', '<h3>Senior Systems Analyst</h3>'),
    ('<p class="ctx">Primeira posição de liderança: responsável pela área de sistemas e desenvolvimento.</p>',
     '<p class="ctx">First leadership role: responsible for the systems and development area.</p>'),
    ('<li>Condução técnica do time e <b>priorização de demandas</b> da área.</li>', '<li>Technical leadership of the team and <b>demand prioritization</b> for the area.</li>'),
    ('<li>Sustentação do Protheus em financeiro, fiscal, suprimentos, produção e RH.</li>', '<li>Ran Protheus across finance, tax, procurement, manufacturing and HR.</li>'),
    ('<li>Desenvolvimento do <b>Portal do Fornecedor</b> integrado ao ERP.</li>', '<li>Built the <b>Supplier Portal</b> integrated with the ERP.</li>'),
    ('<p class="org">BMB Mode Center e BMB Tech · ecossistema MAN / Volkswagen Caminhões e Ônibus</p>',
     '<p class="org">BMB Mode Center and BMB Tech · MAN / Volkswagen Trucks and Buses ecosystem</p>'),
    ('<h3>Gerente de Tecnologia e Inovação</h3>', '<h3>Technology and Innovation Manager</h3>'),
    ('<div class="ladder" aria-label="Progressão de cargos"><span>Especialista Sênior</span><span>Coordenador de TI</span><span>Head de Tecnologia e Inovação, BMB Tech</span><span class="top">Gerente de Tecnologia e Inovação</span></div>',
     '<div class="ladder" aria-label="Role progression"><span>Senior Specialist</span><span>IT Coordinator</span><span>Head of Technology and Innovation, BMB Tech</span><span class="top">Technology and Innovation Manager</span></div>'),
    ('<p class="ctx">De especialista a gerente em menos de 18 meses, com reporte direto à diretoria e atuação simultânea na frente de produtos digitais.</p>',
     '<p class="ctx">From specialist to manager in under 18 months, reporting directly to the board while also leading the digital products front.</p>'),
    ('<li><b>Roadmap e orçamento</b> da área de tecnologia e inovação.</li>', '<li><b>Roadmap and budget</b> for technology and innovation.</li>'),
    ('<li>Migração do ERP e reestruturação de infraestrutura <b>conduzidas pela equipe interna</b>, sem consultoria externa.</li>',
     '<li>ERP migration and infrastructure overhaul <b>delivered by the in-house team</b>, with no outside consultancy.</li>'),
    ('<li>Plataforma web e mobile de <b>indicadores de produção, faturamento e despesas</b> integrada ao ERP, com dashboards para a diretoria.</li>',
     '<li>Web and mobile platform for <b>production, billing and expense KPIs</b> integrated with the ERP, with dashboards for the board.</li>'),
    ('<li>Gestão por OKRs, Scrum e Kanban; formação do time em ADVPL, web e mobile.</li>', '<li>Managed with OKRs, Scrum and Kanban; trained the team in ADVPL, web and mobile.</li>'),
    ('<p class="org">Cinbal, Grupo Incoflandres · indústria do aço</p>', '<p class="org">Cinbal, Incoflandres Group · steel industry</p>'),
    ('<h3>Coordenador de Tecnologia e Desenvolvimento</h3>', '<h3>Technology and Development Coordinator</h3>'),
    ('<p class="ctx">Tecnologia da maior empresa de litografia e beneficiamento de aços planos das Américas, reportando à gerência executiva.</p>',
     '<p class="ctx">Technology for the Americas\' largest flat-steel lithography and processing company, reporting to executive management.</p>'),
    ('<li><b>Mais de R$ 1 milhão em custos evitados</b>: migração do ERP, parque de servidores, monitoramento, telefonia e disaster recovery feitos com equipe própria.</li>',
     '<li><b>More than R$ 1 million in avoided costs</b>: ERP migration, server fleet, monitoring, telephony and disaster recovery delivered by the in-house team.</li>'),
    ('<li>Gestão do <b>orçamento de tecnologia</b> e análise de risco e viabilidade para decisões de investimento.</li>',
     '<li>Managed the <b>technology budget</b> and ran risk and feasibility analysis for investment decisions.</li>'),
    ('<li>Evolução do Protheus: novos módulos, customizações, integradores e sustentação do SQL Server.</li>',
     '<li>Evolved Protheus: new modules, customizations, integrations and SQL Server operations.</li>'),
    ('<p class="org">TOTVS S/A · maior empresa de software do Brasil</p>', '<p class="org">TOTVS S/A · Brazil\'s largest software company</p>'),
    ('<h3>Coordenador de Cloud</h3>', '<h3>Cloud Operations Coordinator</h3>'),
    ('<p class="ctx">Operação Cloud das linhas TOTVS Fluig e TOTVS Agro, com responsabilidade sobre time, indicadores, eficiência operacional e experiência do cliente.</p>',
     '<p class="ctx">Cloud operation for the TOTVS Fluig and TOTVS Agro product lines, accountable for team, KPIs, operational efficiency and customer experience.</p>'),
    ('<li><b>De 400 para mais de 1.500 clientes</b> sem aumento de equipe, com automação e IA incorporadas à rotina.</li>',
     '<li><b>From 400 to more than 1,500 customers</b> with no added headcount, with automation and AI built into the routine.</li>'),
    ('<li>Ambientes críticos com <b>metas de SLA e TMR cumpridas</b> de forma consistente, apoiadas em gestão de risco e prevenção.</li>',
     '<li>Critical environments <b>consistently meeting SLA and MTTR targets</b>, backed by risk management and prevention.</li>'),
    ('<li>Atuação direta em <b>redução de churn</b> e modelos de atendimento para contas estratégicas.</li>',
     '<li>Hands-on <b>churn reduction</b> and service models for strategic accounts.</li>'),
    ('<li>Estruturação do Cloud para o ERP TOTVS Agro, migrações on-premises para Cloud e entre edges, e transição dos ambientes PaaS para <b>Docker e Kubernetes</b>.</li>',
     '<li>Built the Cloud offering for the TOTVS Agro ERP, on-premises to Cloud and cross-edge migrations, and moved PaaS environments to <b>Docker and Kubernetes</b>.</li>'),
    ('<li>Gestão de crise com causa raiz e prevenção de recorrência, junto a Governança e Segurança da Informação.</li>',
     '<li>Crisis management with root cause analysis and recurrence prevention, together with Governance and Information Security.</li>'),

    # ---- projects ----
    ('<h2>Projetos de destaque</h2>', '<h2>Selected projects</h2>'),
    ('Entregas que mudaram a forma como as empresas operam, conduzidas com equipe interna e integradas ao ERP.',
     'Deliveries that changed how companies operate, led with in-house teams and integrated with the ERP.'),
    ('<h3>Monte Sua Solução: configurador de caminhões</h3><p>Configurador online em que o cliente monta o próprio caminhão escolhendo segmento, modelo e componentes. Integrado diretamente ao TOTVS Protheus: respeita as regras de estrutura de produto da tabela SG1 e entra no módulo de vendas como pedido de cotação. <a href="https://www.modecenter.com.br/solucao" target="_blank" rel="noopener">Ver no site da BMB</a></p>',
     '<h3>Monte Sua Solução: truck configurator</h3><p>Online configurator where customers build their own truck by choosing segment, model and components. Integrated directly with TOTVS Protheus: it enforces the bill-of-materials rules in the SG1 table and lands in the sales module as a quotation request. <a href="https://www.modecenter.com.br/solucao" target="_blank" rel="noopener">View on BMB\'s website</a></p>'),
    ('<h3>ROTA: produção em tempo real</h3><p>Plataforma de monitoramento sincronizada com o ERP, mostrando toda a trajetória de produção do veículo, do pedido de venda ao faturamento.</p>',
     '<h3>ROTA: real-time production</h3><p>Monitoring platform synchronized with the ERP, tracking each vehicle\'s full production path, from sales order to invoicing.</p>'),
    ('<h3>Planejamento e controle orçamentário</h3><p>Implantação do PCO com orçado e realizado por centro de custo em dashboard dinâmico. Os dados passaram a alimentar modelos de machine learning para prever orçamentos e investimentos.</p>',
     '<h3>Budget planning and control</h3><p>Rolled out budget planning with budget versus actuals by cost center in a dynamic dashboard. The data now feeds machine learning models that forecast budgets and investments.</p>'),
    ('<h3>Controle de alçada em compras</h3><p>Hierarquia de aprovação por faixa de valor e por orçamento em todo o processo de compras e suprimentos.</p>',
     '<h3>Purchase approval workflows</h3><p>Approval hierarchy by value range and budget across the entire procurement process.</p>'),
    ('<h3>Estoque, custos e PCP</h3><p>Reformulação do controle de estoque com lote e endereçamento, e migração da gestão de projetos para o PCP com o menor impacto possível na operação.</p>',
     '<h3>Inventory, costing and production planning</h3><p>Redesigned inventory control with lot and location tracking, and moved project management into production planning with minimal impact on operations.</p>'),
    ('<h3>Implantações e novos sistemas</h3><p>TOTVS RM Educacional, folha de pagamento ADP, ponto eletrônico e o sistema de admissão do Projeto Capacita, da inscrição à classificação.</p>',
     '<h3>Implementations and new systems</h3><p>TOTVS RM Educational, ADP payroll, time tracking and the Projeto Capacita admissions system, from enrollment to final ranking.</p>'),
    ('<small>Várias empresas</small>', '<small>Several companies</small>'),
    ('<h3>Migrações de plataforma</h3><p>Mais de dez migrações de release ao longo da carreira, entre elas Protheus 10 para 11 e 11 para 12, e SQL Server 2000 para 2016.</p>',
     '<h3>Platform migrations</h3><p>More than ten release migrations over my career, including Protheus 10 to 11 and 11 to 12, and SQL Server 2000 to 2016.</p>'),

    # ---- AI ----
    ('<h2>IA dentro do ERP, não ao lado dele</h2>', '<h2>AI inside the ERP, not next to it</h2>'),
    ('Em paralelo à operação, conduzo iniciativas próprias que aproximam inteligência artificial da realidade das empresas que rodam TOTVS.',
     'Alongside operations, I run my own initiatives that bring artificial intelligence into the reality of companies running TOTVS.'),
    ('Primeiro modelo público de IA especializado em ADVPL e TLPP no Hugging Face, treinado com mais de 150 mil exemplos de desenvolvimento, banco de dados e regras de negócio. Roda localmente e é aberto à comunidade. <a href="https://huggingface.co/dyulianocecilio" target="_blank" rel="noopener">Ver no Hugging Face</a>',
     'The first public AI model specialized in ADVPL and TLPP, the Protheus programming languages, on Hugging Face. Trained on more than 150,000 examples of development, database and business rules. Runs locally and is open to the community. <a href="https://huggingface.co/dyulianocecilio" target="_blank" rel="noopener">View on Hugging Face</a>'),
    ('Plataforma de gestão de equipes multidisciplinares, pensada para times que trabalham nos modelos remoto e híbrido.',
     'Management platform for multidisciplinary teams, designed for remote and hybrid work.'),
    ('<h3>Sistemas executivos de gestão</h3>', '<h3>Executive management systems</h3>'),
    ('Concepção e desenvolvimento de sistemas e aplicativos de gestão para executivos, publicados na App Store e no Google Play.',
     'Designed and built management systems and apps for executives, published on the App Store and Google Play.'),
    ('aria-label="Exemplo de uso do modelo ADVPL AI gerando um ponto de entrada em ADVPL"', 'aria-label="Example of the ADVPL AI model generating an ADVPL entry point"'),
    ("'Crie um ponto de entrada que bloqueie o pedido de venda quando o cliente estiver com crédito vencido.\\n\\n'",
     "'Write an entry point that blocks the sales order when the customer\\'s credit limit has expired.\\n\\n'"),
    ("'// Ponto de entrada MT410TOK: validação na gravação do pedido\\n'", "'// MT410TOK entry point: validation when the order is saved\\n'"),

    # ---- skills ----
    ('<h2>Repertório</h2>', '<h2>Expertise</h2>'),
    ('Domínio técnico profundo, usado a serviço de decisões de negócio.', 'Deep technical command, put to work for business decisions.'),
    ('<h3>TOTVS Protheus</h3><p>Arquitetura, administração, mais de 10 migrações de release, ADVPL e TLPP, APIs e SQL. Processos financeiro, fiscal, contábil, suprimentos, estoque e custos, PCP e RH.</p>',
     '<h3>TOTVS Protheus ERP</h3><p>Architecture, administration, more than 10 release migrations, ADVPL and TLPP, APIs and SQL. Finance, tax, accounting, procurement, inventory and costing, production planning and HR processes.</p>'),
    ('<h3>Gestão de pessoas</h3><p>Formação de analistas e desenvolvedores, mentoria, planos de carreira, avaliação de desempenho e promoção de talentos.</p>',
     '<h3>People management</h3><p>Developing analysts and engineers, mentoring, career plans, performance reviews and talent promotion.</p>'),
    ('<h3>Operações e resultados</h3><p>SLA e TMR, gestão de capacidade, custo operacional, retenção de clientes e gestão de crise.</p>',
     '<h3>Operations and results</h3><p>SLA and MTTR, capacity management, operating cost, customer retention and crisis management.</p>'),
    ('<h3>Estratégia e governança</h3><p>Roadmap, priorização, viabilidade e risco, orçamento de tecnologia, reporte à diretoria, governança e segurança da informação.</p>',
     '<h3>Strategy and governance</h3><p>Roadmap, prioritization, feasibility and risk, technology budget, board reporting, governance and information security.</p>'),
    ('<h3>IA e automação</h3><p>LLMs, fine-tuning de modelos, IA local, agentes, automação de operações e adoção de IA pelas equipes.</p>',
     '<h3>AI and automation</h3><p>LLMs, model fine-tuning, local AI, agents, operations automation and AI adoption across teams.</p>'),
    ('<h3>Engenharia</h3><p>C#, Node.js, TypeScript, React, React Native, Flutter, SQL Server, Docker, Kubernetes, BI e TOTVS Fluig.</p>',
     '<h3>Engineering</h3><p>C#, Node.js, TypeScript, React, React Native, Flutter, SQL Server, Docker, Kubernetes, BI and TOTVS Fluig.</p>'),
    ('<h3>Formação</h3>', '<h3>Education</h3>'),
    ('<dt>MBA Executivo em Inteligência Artificial Aplicada a Negócios</dt>', '<dt>Executive MBA, Artificial Intelligence Applied to Business</dt>'),
    ('<dt>Pós-graduação em Engenharia de Software</dt>', '<dt>Postgraduate degree, Software Engineering</dt>'),
    ('<dt>Extensão em Business Intelligence</dt>', '<dt>Extension program, Business Intelligence</dt>'),
    ('<dt>Extensão em BI e Data Science</dt>', '<dt>Extension program, BI and Data Science</dt>'),
    ('<dt>Bacharelado em Sistemas de Informação</dt>', '<dt>Bachelor\'s degree, Information Systems</dt>'),
    ('<h3>Liderança e certificações</h3>', '<h3>Leadership and certifications</h3>'),
    ('<dt>Programa Fora da Curva</dt>', '<dt>Fora da Curva leadership program</dt>'),
    ('<dt>TOTVS Fluig, Plataforma e Negócio</dt>', '<dt>TOTVS Fluig, Platform and Business</dt>'),
    ('<dt>Programação ADVPL</dt>', '<dt>ADVPL Programming</dt>'),
    ('<dt>ASP.NET Razor, Flutter e Vue.js</dt><dd>Formações técnicas</dd>', '<dt>ASP.NET Razor, Flutter and Vue.js</dt><dd>Technical programs</dd>'),

    # ---- footer ----
    ('<p class="foot-role">Liderança em tecnologia, operações Cloud, ERP e IA aplicada. Brasil.</p>',
     '<p class="foot-role">Technology leadership, Cloud operations, ERP and applied AI. Brazil.</p>'),
    ('<nav class="foot-links" aria-label="Contato">', '<nav class="foot-links" aria-label="Contact">'),
    ('<a href="assets/Dyuliano-Cecilio-Curriculo.pdf" download>Currículo em PDF</a>', '<a href="../assets/Dyuliano-Cecilio-Resume.pdf" download>Résumé (PDF)</a>'),
    ('<a href="#inicio">Voltar ao topo</a>', '<a href="#inicio">Back to top</a>'),

    # ---- number formatting ----
    ("n.toLocaleString('pt-BR')", "n.toLocaleString('en-US')"),
]


def main():
    src = (ROOT / 'index.html').read_text(encoding='utf-8')
    out = src
    missing = []
    for pt, en in PAIRS:
        if pt not in out:
            missing.append(pt)
            continue
        out = out.replace(pt, en)
    if missing:
        print('Textos em português não encontrados no index.html (atualize o par em tools/build_en.py):', file=sys.stderr)
        for m in missing:
            print('  -', m[:120], file=sys.stderr)
        sys.exit(1)
    dest = ROOT / 'en' / 'index.html'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(out, encoding='utf-8')
    print(f'ok: {dest.relative_to(ROOT)} ({len(PAIRS)} trechos traduzidos)')


if __name__ == '__main__':
    main()
