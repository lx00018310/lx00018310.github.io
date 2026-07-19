from playwright.sync_api import sync_playwright
import os

def html_to_pdf(html_path, pdf_path):
    abs_html = os.path.abspath(html_path)
    file_url = f'file:///{abs_html.replace(os.sep, "/")}'
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_url, wait_until='networkidle')
        page.pdf(
            path=pdf_path,
            format='A4',
            margin={
                'top': '20mm',
                'right': '22mm',
                'bottom': '20mm',
                'left': '22mm'
            },
            print_background=True,
            prefer_css_page_size=True
        )
        browser.close()
    print(f"PDF生成成功: {pdf_path}")

if __name__ == '__main__':
    html_file = os.path.join(os.path.dirname(__file__), '..', 'docs', 'assets', 'resume.html')
    pdf_file = os.path.join(os.path.dirname(__file__), '..', 'docs', 'assets', 'resume.pdf')
    html_to_pdf(html_file, pdf_file)
