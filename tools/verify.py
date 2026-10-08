#!/usr/bin/env python3
"""按中英文定稿首页检查当前作品集内容、资源、PDF 与浏览器表现。

用法：python -X utf8 tools/verify.py
检查失败或依赖缺失均返回非零退出码，不跳过检查。
"""
import functools
from collections import Counter
import json
import re
import sys
import threading
import xml.etree.ElementTree as ET
from html import unescape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from PIL import Image
from pypdf import PdfReader
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://lx00018310.github.io/"
HOMES = ["index.html", "index-en.html"]
PAGES = HOMES + ["assets/resume.html"]
results = []


def read(path):
    return path.read_text(encoding="utf-8")


def soup(path):
    return BeautifulSoup(read(path), "html.parser")


def normalize(text):
    return re.sub(r"[\W_]+", "", unescape(text)).lower()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check(name, fn):
    try:
        evidence = fn()
        results.append((True, name, evidence))
    except Exception as exc:
        results.append((False, name, str(exc)))


def projects(page):
    return [(x.select_one(".showcase-pinned-title").get_text(" ", strip=True),
             x.select_one(".showcase-pinned-tagline").get_text(" ", strip=True),
             x.select_one(".showcase-pinned-lead").get_text(" ", strip=True))
            for x in page.select(".showcase-layer")]


def check_homes():
    for filename, language, email, titles in [
        (HOMES[0], "zh-CN", "dzpdd@163.com", ["考亭古街", "数字月台", "EmergentInc"]),
        (HOMES[1], "en", "lx00018310@gmail.com", ["Kaoting Ancient Street", "Digital Loading Dock", "EmergentInc"]),
    ]:
        page = soup(DOCS / filename)
        require(page.html["lang"] == language, f"{filename}: language")
        require(len(page.find_all("h1")) == 1, f"{filename}: H1 count")
        require([x[0] for x in projects(page)] == titles, f"{filename}: project order")
        link = page.select_one(".gf-email-headline")
        require(link.get_text(strip=True) == email and link["href"] == "mailto:" + email,
                f"{filename}: email text / target")
        require("18761576008" in page.select_one(".contact-modal").get_text(), f"{filename}: phone")
        require(page.select_one('a[href="assets/resume.pdf"][download]'), f"{filename}: PDF download")
        for anchor in ["overview", "tourism", "industrial", "emergentinc", "contact"]:
            require(page.find(id=anchor), f"{filename}: missing #{anchor}")
    return "中英文身份、项目顺序、联系与下载入口正确"


def check_jsonld():
    expected_roles = ["AI 顾问", "AI Consultant & Solutions Architect"]
    knowledge = []
    for filename, role in zip(HOMES, expected_roles):
        page = soup(DOCS / filename)
        data = json.loads(page.select_one('script[type="application/ld+json"]').string)
        nodes = {x["@type"]: x for x in data["@graph"]}
        require({"Person", "WebSite"} <= nodes.keys(), f"{filename}: schema types")
        require(nodes["Person"]["jobTitle"] == role, f"{filename}: role")
        knowledge.append(nodes["Person"]["knowsAbout"])
        url = SITE if filename == "index.html" else SITE + filename
        require(page.select_one('link[rel="canonical"]')["href"] == url, f"{filename}: canonical")
        require(page.select_one('meta[property="og:url"]')["content"] == url, f"{filename}: OG URL")
        require(page.title.get_text() == page.select_one('meta[property="og:title"]')["content"], f"{filename}: title")
        require(page.select_one('meta[property="og:description"]')["content"] ==
                page.select_one('meta[name="twitter:description"]')["content"], f"{filename}: social description")
    require(knowledge[0] == knowledge[1], "中英文知识领域不一致")
    return "JSON-LD、语言对应职位、canonical 和分享元数据一致"


def check_content():
    zh, en = [projects(soup(DOCS / f)) for f in HOMES]
    profile = normalize(read(DOCS / "ai-profile.md"))
    for title, tagline, lead in zh + en:
        require(all(normalize(x) in profile for x in (title, tagline, lead)), f"ai-profile.md: {title}")
    # README 是定稿摘要：逐字保留首页各项目的标题、slogan 与正文
    readme = normalize(read(ROOT / "README.md"))
    for title, tagline, lead in zh:
        require(all(normalize(x) in readme for x in (title, tagline, lead)), f"README.md: {title}")
    # 简历面向 HR / 老板，用更直白的语言表达同一批事实：项目顺序一致、关键结果与技能齐备即可
    resume = soup(DOCS / "assets/resume.html")
    require([x.select_one(".project-head span").get_text(strip=True) for x in resume.select(".project-card")] ==
            [x[0] for x in zh], "简历项目顺序与首页不一致")
    restext = normalize(resume.get_text(" "))
    for title, facts in [("考亭古街", ["212万"]), ("数字月台", ["真机上线", "验收", "plc"]),
                         ("EmergentInc", ["开源", "自动赚钱"])]:
        require(normalize(title) in restext, f"简历缺少项目名：{title}")
        require(all(normalize(f) in restext for f in facts), f"简历项目 {title} 缺少关键事实")
    for path in [ROOT / "README.md", DOCS / "ai-profile.md", DOCS / "llms.txt"]:
        text = read(path)
        for term in ["升维看", "多维做", "Think Higher", "Build Wider", "dzpdd@163.com", "lx00018310@gmail.com", "18761576008"]:
            require(term in text, f"{path.name}: missing {term}")
        for _, tagline, _ in zh:
            require(tagline in text, f"{path.name}: missing {tagline}")
    return "README、AI 档案、llms 与首页定稿一致；简历以直白语言保留项目顺序与关键结果"


def check_stale_content():
    obsolete = ["624290365@qq.com", "AI 产品经理", "IRO_agent", "ToyWake", "SimpleHmi", "天津机器人产线",
                "湖州美食地图", "文旅溯源地", "快速 PoC", "12 台 HMI", "全网回滚 < 90", "事故 0 起"]
    paths = [ROOT / "README.md"] + list(DOCS.rglob("*")) + [ROOT / "tools" / p for p in
            ["og.html", "generate_visuals.py", "generate_images.py", "html_to_pdf.py"]]
    hits = []
    for path in paths:
        if path.is_file() and path.suffix in {".md", ".html", ".txt", ".svg", ".py"}:
            for term in obsolete:
                if term in read(path):
                    hits.append(f"{path.relative_to(ROOT)}: {term}")
    require(not hits, "; ".join(hits))
    return "公开材料与生成模板未残留旧邮箱、旧定位、旧案例及旧项目叙事"


def resolve(origin, url):
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        if parsed.netloc != urlsplit(SITE).netloc:
            return None, ""
        target = DOCS / (unquote(parsed.path).lstrip("/") or "index.html")
    else:
        path = unquote(parsed.path)
        target = DOCS / path.lstrip("/") if path.startswith("/") else origin.parent / path if path else origin
    return target.resolve(), unquote(parsed.fragment)


def check_links():
    paths = list(DOCS.rglob("*.html")) + [ROOT / "tools/og.html"]
    count = 0
    for path in paths:
        page = soup(path)
        ids = [x["id"] for x in page.find_all(id=True)]
        require(len(ids) == len(set(ids)), f"{path.name}: duplicate IDs")
        urls = [x[attr] for x in page.find_all() for attr in ("href", "src") if x.has_attr(attr)]
        urls += re.findall(r"url\(['\"]?([^)'\"]+)['\"]?\)", read(path))
        for link in page.select('a[href^="mailto:"]'):
            require(link.get_text(strip=True) == link["href"][7:], f"{path.name}: mismatched mailto")
        for url in urls:
            target, fragment = resolve(path, url)
            if target is None:
                continue
            require(target.is_file(), f"{path.name}: missing {url}")
            if fragment and target.suffix == ".html":
                require(soup(target).find(id=fragment), f"{path.name}: missing anchor {url}")
            count += 1
    for path in [ROOT / "README.md", DOCS / "ai-profile.md", DOCS / "llms.txt", DOCS / "assets/site.css"]:
        pattern = r"url\(['\"]?([^)'\"]+)['\"]?\)" if path.suffix == ".css" else r"https://lx00018310\.github\.io/[^\s)\]<>]*|(?<=\]\()[^)]+"
        for url in re.findall(pattern, read(path)):
            target, fragment = resolve(path, url)
            if target is None:
                continue
            require(target.is_file(), f"{path.name}: missing {url}")
            if fragment and target.suffix == ".html":
                require(soup(target).find(id=fragment), f"{path.name}: missing #{fragment}")
            count += 1
    return f"{count} 个内部页面、资源与锚点引用均存在，无重复 ID"


def check_sitemap():
    tree = ET.parse(DOCS / "sitemap.xml")
    locs = [x.text for x in tree.findall(".//{*}loc")]
    require(locs == [SITE, SITE + HOMES[1], SITE + PAGES[2]], "sitemap 不符合当前公开页面清单")
    for url in locs:
        target, _ = resolve(DOCS / "index.html", url)
        require(target.is_file(), f"sitemap: {url}")
    require("Sitemap: " + SITE + "sitemap.xml" in read(DOCS / "robots.txt"), "robots sitemap")
    return "网站地图仅包含当前三个公开内容页面，robots 引用正确"


def check_visuals():
    require(Image.open(DOCS / "assets/og-home.png").size == (1200, 630), "OG size")
    template = soup(ROOT / "tools/og.html")
    require([x["id"] for x in template.select(".og")] == ["og-home"], "分享模板仍包含旧案例")
    for term in ["升维看", "多维做", "Think Higher", "Build Wider", "212", "EmergentInc"]:
        require(term in template.get_text(), f"OG missing {term}")
    for file, terms in [("dock-system.svg", ["移动机器人", "PLC", "统一状态", "验收"]),
                        ("dock-system-en.svg", ["Mobile Robots", "PLCs", "Unified state", "acceptance"])]:
        path = DOCS / "assets/visuals" / file
        ET.parse(path)
        for term in terms:
            require(term in read(path), f"{file}: {term}")
    require("dock-system-en.svg" in read(DOCS / HOMES[1]), "英文首页未使用英文拓扑图")
    return "分享图 1200×630，拓扑图具备 PLC、机器人及中英文对应叙事"


def check_pdf():
    pdf = PdfReader(DOCS / "assets/resume.pdf")
    require(len(pdf.pages) == 2, f"PDF pages: {len(pdf.pages)}")
    page = soup(DOCS / "assets/resume.html")
    sections = page.select(".resume-page")
    require(len(sections) == len(pdf.pages), "HTML 与 PDF 页数不同")
    for i, (section, printed) in enumerate(zip(sections, pdf.pages)):
        expected = normalize(section.get_text(" "))
        actual = normalize(printed.extract_text())
        require(Counter(expected) == Counter(actual), f"PDF 第 {i+1} 页存在缺失或额外文字")
        # Chromium 会将定位页眉写入正文之后；逐字核对后单独比较正文顺序。
        header = section.find("header")
        if header:
            header_text = normalize(header.get_text(" "))
            require(header_text in actual, "PDF 页眉文字不完整")
            expected = expected.replace(header_text, "", 1)
            actual = actual.replace(header_text, "", 1)
        require(expected == actual, f"PDF 第 {i+1} 页正文与 HTML 不一致")
    links = [str(a.get_object().get("/A", {}).get("/URI", "")) for p in pdf.pages for a in p.get("/Annots", [])]
    require("mailto:dzpdd@163.com" in links, "PDF mailto")
    return "PDF 为两页，全文与 HTML 相同，邮箱链接正确"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def check_browser():
    handler = functools.partial(QuietHandler, directory=str(DOCS))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}/"
    errors = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for width in [375, 1440]:
                page = browser.new_page(viewport={"width": width, "height": 900})
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
                for filename in PAGES:
                    response = page.goto(base + filename, wait_until="networkidle")
                    require(response.status == 200, f"{filename}: HTTP")
                    page.evaluate("document.fonts.ready")
                    require(page.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1"),
                            f"{filename}: overflow at {width}px")
                    require(page.locator("img").evaluate_all("els => els.every(e => e.complete && e.naturalWidth > 0)"),
                            f"{filename}: broken image")
                    if filename in HOMES:
                        require(page.locator("#showcase-layer-1 img").evaluate("e => getComputedStyle(e).objectFit") == "contain",
                                f"{filename}: 拓扑图存在裁切")
                        page.locator("#wechat-phone-link").click()
                        require(page.locator("#contact-modal").get_attribute("aria-hidden") == "false", f"{filename}: modal open")
                        page.keyboard.press("Escape")
                        require(page.locator("#contact-modal").get_attribute("aria-hidden") == "true", f"{filename}: modal close")
                page.close()
            page = browser.new_page()
            page.goto(base + "assets/resume.html", wait_until="networkidle")
            page.emulate_media(media="print")
            require(not page.locator(".toolbar").is_visible(), "简历打印工具栏未隐藏")
            for i, section in enumerate(page.locator(".resume-page").all()):
                require(section.evaluate("e => e.scrollHeight <= e.clientHeight + 1"), f"简历第 {i+1} 页打印内容溢出")
            page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    require(not errors, "; ".join(errors[:5]))
    return "三个页面在 375px / 1440px 无横向溢出、图片失败或 JS 错误；联系弹窗与简历打印正常"


def main():
    for name, fn in [("首页与联系", check_homes), ("结构化数据", check_jsonld),
                     ("跨文件内容一致性", check_content), ("旧内容扫描", check_stale_content),
                     ("链接与资源", check_links), ("网站地图", check_sitemap),
                     ("分享图与拓扑图", check_visuals), ("PDF 一致性", check_pdf),
                     ("浏览器 review", check_browser)]:
        check(name, fn)
    for passed, name, evidence in results:
        print(f"[{'通过' if passed else '未通过'}] {name}: {evidence}")
    failed = sum(not passed for passed, _, _ in results)
    print(f"通过 {len(results)-failed} 项，未通过 {failed} 项，跳过 0 项")
    return int(bool(failed))


if __name__ == "__main__":
    sys.exit(main())
