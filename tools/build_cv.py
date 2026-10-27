"""Gera os currículos em PDF (PT e EN) prontos para recrutadores, ATS e IA.

    pip install pypdf pypdfium2 pillow
    python3 tools/build_cv.py

- PDF com texto real e marcado (tagged), sumário de seções e links clicáveis;
- metadados de título, autor, assunto, palavras-chave e idioma;
- miniaturas das páginas para a seção de download do site.
"""
import pathlib
import subprocess

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

KEYWORDS = ('Gestão de Tecnologia, Liderança de Times, Operações Cloud, TOTVS Protheus, ADVPL, TLPP, ERP, '
            'Migração de ERP, SLA, TMR, Churn, Orçamento de TI, Governança, IA Aplicada, LLM, Automação, '
            'SQL Server, Docker, Kubernetes, TOTVS Fluig, TOTVS RM')
KEYWORDS_EN = ('Technology Management, Team Leadership, Cloud Operations, TOTVS Protheus, ADVPL, TLPP, ERP, '
               'ERP Migration, SLA, MTTR, Churn, IT Budget, Governance, Applied AI, LLM, Automation, '
               'SQL Server, Docker, Kubernetes, TOTVS Fluig, TOTVS RM')

CVS = [
    ('cv-pt.html', 'Dyuliano-Cecilio-Curriculo.pdf', 'pt-BR', 'cv-pt',
     'Dyuliano Cecilio de Souza — Currículo',
     'Liderança em Tecnologia, Operações Cloud, ERP TOTVS Protheus e IA aplicada', KEYWORDS),
    ('cv-en.html', 'Dyuliano-Cecilio-Resume.pdf', 'en-US', 'cv-en',
     'Dyuliano Cecilio de Souza — Résumé',
     'Technology Leadership, Cloud Operations, TOTVS Protheus ERP and Applied AI', KEYWORDS_EN),
]


def main():
    for src, out, lang, thumb, title, subject, keywords in CVS:
        pdf = ROOT / 'assets' / out
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                        '--export-tagged-pdf', '--generate-pdf-document-outline',
                        '--virtual-time-budget=8000', f'--print-to-pdf={pdf}', (TOOLS / src).as_uri()],
                       check=True, capture_output=True)
        reader = PdfReader(pdf)
        writer = PdfWriter(clone_from=reader)
        writer.add_metadata({'/Title': title, '/Author': 'Dyuliano Cecilio de Souza', '/Subject': subject,
                             '/Keywords': keywords, '/Creator': 'dyuliano.github.io'})
        writer._root_object[NameObject('/Lang')] = TextStringObject(lang)
        with open(pdf, 'wb') as f:
            writer.write(f)
        pages = len(PdfReader(pdf).pages)
        print(f'ok: {out} ({pages} páginas)')
        try:
            import pypdfium2 as pdfium
            doc = pdfium.PdfDocument(str(pdf))
            for i, suffix in ((0, ''), (1, '-2')):
                if i < len(doc):
                    img = doc[i].render(scale=600 / doc[i].get_width()).to_pil().convert('RGB')
                    img.save(ROOT / 'assets' / f'{thumb}{suffix}.jpg', quality=84, optimize=True)
        except ImportError:
            print('  (sem pypdfium2: miniaturas não geradas)')


if __name__ == '__main__':
    main()
