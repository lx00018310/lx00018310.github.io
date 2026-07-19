import markdown
from weasyprint import HTML, CSS
import os

def convert_md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content, extensions=['extra', 'toc', 'tables'])
    
    full_html = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>董达｜AI 智能自动化工程师简历</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    css = CSS(string='''
        @page {
            size: A4;
            margin: 2cm 2.2cm;
            @top-center {
                content: "董达｜AI 智能自动化工程师";
                font-family: "Microsoft YaHei", sans-serif;
                font-size: 10px;
                color: #666;
            }
            @bottom-right {
                content: counter(page) " / " counter(pages);
                font-family: "Microsoft YaHei", sans-serif;
                font-size: 9px;
                color: #999;
            }
        }
        
        * {
            box-sizing: border-box;
        }
        
        body {
            font-family: "Microsoft YaHei", "Segoe UI", Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.65;
            color: #1d1d1d;
            background: #fff;
        }
        
        h1 {
            font-size: 24pt;
            font-weight: 900;
            color: #000;
            border-bottom: 4px solid #000;
            padding-bottom: 10px;
            margin: 0 0 12px;
            letter-spacing: -0.5px;
        }
        
        h2 {
            font-size: 15pt;
            font-weight: 900;
            background: #000;
            color: #fff;
            display: inline-block;
            padding: 4px 12px;
            margin: 22px 0 14px;
        }
        
        h3 {
            font-size: 13pt;
            font-weight: 900;
            color: #000;
            border-left: 5px solid #000;
            padding-left: 10px;
            margin: 18px 0 10px;
        }
        
        p {
            margin: 8px 0;
            text-align: justify;
        }
        
        strong {
            font-weight: 900;
            color: #000;
        }
        
        ul {
            margin: 8px 0;
            padding-left: 22px;
        }
        
        li {
            margin: 6px 0;
            line-height: 1.7;
        }
        
        hr {
            border: none;
            border-top: 2px solid #000;
            margin: 24px 0;
        }
        
        /* 联系信息样式 */
        h1 + p {
            font-size: 11pt;
            font-weight: 700;
            margin-bottom: 6px;
        }
        
        h1 + p + p {
            font-size: 10.5pt;
            color: #444;
            font-weight: 700;
        }
        
        /* 核心优势列表 */
        ul li strong {
            background: #f0f0ed;
            padding: 1px 4px;
        }
        
        /* 项目标题样式 */
        h3 + p {
            font-size: 10.5pt;
            color: #555;
            font-style: italic;
        }
    ''')
    
    HTML(string=full_html).write_pdf(pdf_path, stylesheets=[css])
    print(f"PDF generated: {pdf_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    md_path = os.path.join(base_dir, "docs", "assets", "resume.md")
    pdf_path = os.path.join(base_dir, "docs", "assets", "resume.pdf")
    convert_md_to_pdf(md_path, pdf_path)
