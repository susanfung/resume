import os
import weasyprint
from jinja2 import Environment, FileSystemLoader

ROOT = '/Users/susanfung/Documents/GitLab/Resume'
ASSETS_DIR = os.path.join(ROOT, 'assets')

TEMPLAT_SRC = os.path.join(ROOT, './')
CSS_SRC = os.path.join(ROOT, 'static/css')
DEST_DIR = os.path.join(ROOT, 'output')

TEMPLATE = 'index.html'
CSS = 'style.css'
OUTPUT_FILENAME = 'My-Resume.pdf'

def start():
    print('start generate report...')
    env = Environment(loader=FileSystemLoader(TEMPLAT_SRC))
    template = env.get_template(TEMPLATE)
    css = os.path.join(CSS_SRC, CSS)

    # variables
    template_vars = { 'assets_dir': 'file://' + ASSETS_DIR }

    # rendering to html string
    rendered_string = template.render(template_vars)
    html = weasyprint.HTML(string=rendered_string)
    report = os.path.join(DEST_DIR, OUTPUT_FILENAME)
    html.write_pdf(report, stylesheets=[css])
    print('file is generated successfully and under {}', DEST_DIR)


if __name__ == '__main__':
    start()