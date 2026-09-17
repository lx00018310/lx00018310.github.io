from playwright.sync_api import sync_playwright
import os
import sys

def html_to_pdf(html_path, pdf_path, margin=None):
    abs_html = os.path.abspath(html_path)
    file_url = f'file:///{abs_html.replace(os.sep, "/")}'
    
    # 默认边距匹配计划书第 4.1 / 8 节；若调用方传入则覆盖
    pdf_kwargs = {
        'format': 'A4',
        'print_background': True,
        'prefer_css_page_size': True
    }
    if margin is not None:
        pdf_kwargs['margin'] = margin

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_url, wait_until='networkidle')
        page.pdf(path=pdf_path, **pdf_kwargs)
        browser.close()
    print(f"PDF生成成功: {pdf_path}")

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        html_file = sys.argv[1]
        pdf_file = sys.argv[2]
    else:
        html_file = os.path.join(os.path.dirname(__file__), '..', 'docs', 'assets', 'resume.html')
        pdf_file = os.path.join(os.path.dirname(__file__), '..', 'docs', 'assets', 'resume.pdf')
    html_to_pdf(html_file, pdf_file)
