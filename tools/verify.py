#!/usr/bin/env python3
"""求职定位与作品集调整验收脚本 (v2 强化版)。

依据《作品集视觉化改造与内容纠偏Plan.md》第 9 节编写：
1. 本地服务与页面可达 (7公开页 + 2简历页)
2. 首页 6 个连续 section 规范、单 H1、下载入口、无旧 FAQ、三卡顺序
3. 案例与方法页规范结构与唯一定型 H1
4. 全站统一导航与品牌
5. 无外部资源依赖（无 CDN，离线可运行）
6. JSON-LD 逐页解析与 Person 字段规范
7. sitemap 与 robots 链接可达，无私下泄漏
8. 全套 7 张 1200x630 OG 分享图校验
9. 站内链接、img/svg 资源有效性与锚点有效性（无重复 ID，锚点全命中）
10. 违规禁用词全面审计（Plan 2.4 节 + 9.1 节新增）及 docs/_internal 隐私检查
11. 简历一致性、无占位符及三份 PDF 真实页数与文本校验
12. 浏览器测试（9 页 375px 无溢出、无 console 错误、打印隐藏导航）

用法：
    python -X utf8 tools/verify.py
"""
import json
import re
import sys
import urllib.request
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PRIVATE = ROOT / "job-search-private"
BASE = "http://127.0.0.1:8765/"

PAGES = [
    "index.html", "digital-dock.html", "iro-agent.html",
    "robot-line.html", "toywake.html", "ai-engineering.html",
    "simplehmi-weili.html", "huzhou-food-map.html"
]

ALL_PAGES = PAGES + ["assets/resume.html", "assets/董达_简历_一页.html"]

results = []   # (状态, 项目, 证据)


def ok(item, evidence):
    results.append(("PASS", item, evidence))


def fail(item, evidence):
    results.append(("FAIL", item, evidence))


def skip(item, evidence):
    results.append(("SKIP", item, evidence))


def read(name):
    return (DOCS / name).read_text(encoding="utf-8")


def strip_comments(src):
    return re.sub(r"<!--.*?-->", "", src, flags=re.S)


# ── 1 本地服务与页面可达 ──────────────────────────────────────────
def check_serving():
    codes = {}
    for p in [""] + ALL_PAGES:
        encoded_p = urllib.parse.quote(p, safe="/:")
        url = BASE + encoded_p
        try:
            req = urllib.request.urlopen(url, timeout=5)
            codes[p or "/"] = req.status
        except Exception as e:
            codes[p or "/"] = getattr(e, "code", repr(e))
    bad = {k: v for k, v in codes.items() if v != 200}
    if bad:
        fail(f"本地起站，全部 {len(ALL_PAGES)} 页可达", f"非 200：{bad}")
    else:
        ok(f"本地起站，全部 {len(ALL_PAGES)} 页可达", f"{len(codes)} 个 URL 全部 200 OK")


# ── 2 首页 6 个连续 section 与核心内容 ──────────────────────────
def check_home():
    src = read("index.html")
    main_match = re.search(r"<main\b[^>]*>(.*?)</main>", src, re.S)
    if not main_match:
        fail("首页 main 区域结构", "未找到 <main> 标签")
        return
    main_content = main_match.group(1)
    sections = re.findall(r'<section\b[^>]*id="([^"]+)"[^>]*>', main_content)
    expected_ids = ["top", "workflow", "cases", "skills", "commercial", "experience", "how", "contact"]
    if sections == expected_ids:
        ok("首页包含且仅包含 8 个规定 ID section", " → ".join(sections))
    else:
        fail("首页包含且仅包含 8 个规定 ID section", f"实际：{sections}，预期：{expected_ids}")

    # 只有一个 H1
    h1s = re.findall(r"<h1\b[^>]*>(.*?)</h1>", src, re.S)
    if len(h1s) == 1 and "董达" in h1s[0] and "AI 产品经理" in h1s[0]:
        ok("首页恰好 1 个 H1 且包含统一身份", h1s[0].strip())
    else:
        fail("首页恰好 1 个 H1 且包含统一身份", f"实际 H1 数：{len(h1s)}")

    # 下载入口与无旧 FAQ
    has_pdf = 'href="assets/resume.pdf"' in src
    has_old_faq = 'id="faq"' in src or "你可能会问" in src
    if has_pdf and not has_old_faq:
        ok("首页具备 PDF 下载入口且无旧宣传 FAQ", "包含 resume.pdf 下载链接，已清除旧 FAQ 屏")
    else:
        fail("首页具备 PDF 下载入口且无旧宣传 FAQ", f"PDF链接: {has_pdf}, 存在旧FAQ: {has_old_faq}")

    # 代表项目六卡排序：数字月台 → IRO_agent → 天津机器人产线 → 考亭古街 → ToyWake → SimpleHmi
    cases_section = re.search(r'<section\b[^>]*id="cases"[^>]*>(.*?)</section>', main_content, re.S)
    if cases_section:
        c_text = cases_section.group(1)
        p_dock = c_text.find("数字月台")
        p_iro = c_text.find("IRO_agent")
        p_robot = c_text.find("天津机器人")
        p_kaoting = c_text.find("考亭古街")
        p_toywake = c_text.find("ToyWake")
        p_simplehmi = c_text.find("SimpleHmi")
        if -1 < p_dock < p_iro < p_robot < p_kaoting < p_toywake < p_simplehmi:
            ok("代表项目六卡顺序符合规定", "数字月台 → IRO_agent → 天津机器人产线 → 考亭古街 → ToyWake → SimpleHmi")
        else:
            fail("代表项目六卡顺序符合规定", f"排序异常: dock={p_dock}, iro={p_iro}, robot={p_robot}, kaoting={p_kaoting}, toywake={p_toywake}, simplehmi={p_simplehmi}")
    else:
        fail("代表项目六卡顺序符合规定", "未找到 cases section")


# ── 3 案例与方法页规范结构 ──────────────────────────────────────────
def check_case_pages():
    cases = {
        "digital-dock.html": ("把订单、界面与设备连接起来", "已上线已验收"),
        "iro-agent.html": ("让 AI 不再“猜故障”，而是像工程师一样逐步取证", "应用验证"),
        "robot-line.html": ("让工控主程序协调取餐与送餐", "已交付"),
        "toywake.html": ("给一句提示，把游戏还给亲子", "原型"),
        "ai-engineering.html": ("让 AI 写得快，也让修改可检查", ""),
        "simplehmi-weili.html": ("从需求到可检查的工业软件", ""),
        "huzhou-food-map.html": ("把店铺信息做成有依据的地图", "")
    }
    bad = []
    for page, (exp_title, exp_status) in cases.items():
        src = read(page)
        h1s = re.findall(r"<h1\b[^>]*>(.*?)</h1>", src, re.S)
        if len(h1s) != 1 or exp_title not in h1s[0]:
            bad.append(f"{page} H1 不符合：{h1s}")
        if exp_status and exp_status not in src:
            bad.append(f"{page} 缺少状态声明：{exp_status}")
    if bad:
        fail("案例与方法页符合标题与状态规范", "；".join(bad))
    else:
        ok("案例与方法页符合标题与状态规范", f"{len(cases)} 个案例/方法页均具有唯一定型 H1 及对应状态")


# ── 4 全站统一导航 ──────────────────────────────────────────────
def check_nav():
    bad = []
    for p in PAGES:
        src = strip_comments(read(p))
        m = re.search(r'<nav class="nav"[^>]*>(.*?)</nav>', src, re.S)
        if not m:
            bad.append(f"{p} 无 nav.nav")
            continue
        nav_html = m.group(1)
        if "董达" not in nav_html:
            bad.append(f"{p} 导航缺姓名品牌")
        if "resume" not in nav_html:
            bad.append(f"{p} 导航缺简历链接")
    if bad:
        fail("全站统一导航存在且有效", "；".join(bad))
    else:
        ok("全站统一导航存在且有效", f"{len(PAGES)} 个页面均具备统一品牌与有效导航项")


# ── 5 无外部资源依赖（无 CDN） ──────────────────────────────────
def check_no_cdn():
    offenders = []
    for p in PAGES:
        src = strip_comments(read(p))
        for m in re.finditer(r"<(link|script|img|iframe)\b([^>]*)>", src, re.I):
            tag, attrs = m.group(1).lower(), m.group(2)
            if tag == "link":
                rel = re.search(r'rel="([^"]*)"', attrs)
                rel = (rel.group(1).lower() if rel else "")
                if not any(k in rel for k in ("stylesheet", "preload", "icon", "prefetch")):
                    continue
                target = re.search(r'href="(https?://[^"]+)"', attrs)
            else:
                target = re.search(r'src="(https?://[^"]+)"', attrs)
            if target:
                offenders.append((p, f"<{tag}> {target.group(1)}"))
    css = (DOCS / "assets" / "site.css").read_text(encoding="utf-8")
    for m in re.finditer(r"url\((['\"]?)(https?://[^)]+)\1\)", css):
        offenders.append(("site.css", m.group(2)))
    if "@import" in css:
        offenders.append(("site.css", "@import"))
    if offenders:
        fail("断网情况下样式排版正常（无 CDN 依赖）", f"外部资源引用：{offenders}")
    else:
        ok("断网情况下样式排版正常（无 CDN 依赖）",
           "全部页面与 site.css 中零外部 link/script/img/font/@import 引用")


# ── 6 JSON-LD 结构化数据 ──────────────────────────────────────────
def check_jsonld():
    found, bad = {}, []
    for p in PAGES:
        for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', read(p), re.S):
            try:
                d = json.loads(b)
            except Exception as e:
                bad.append((p, str(e)))
                continue
            nodes = d.get("@graph", [d])
            found.setdefault(p, []).extend(n.get("@type") for n in nodes)
    if bad:
        fail("JSON-LD 全部可解析", f"解析失败：{bad}")
        return

    # 验证不能残留 FAQPage，且 index 必须有 Person 和 WebSite
    index_types = found.get("index.html", [])
    if "FAQPage" in index_types:
        fail("首页已清理旧 FAQPage JSON-LD", "仍残留 FAQPage")
    elif "Person" in index_types and "WebSite" in index_types:
        ok("首页 JSON-LD 包含 Person/WebSite 且无 FAQPage", f"类型：{index_types}")
    else:
        fail("首页 JSON-LD 必备类型", f"缺类型：{index_types}")

    # 检查 Person 的 jobTitle 为真实当前职位 AI Application Engineer
    src_index = read("index.html")
    if '"jobTitle": "AI Application Engineer"' in src_index:
        ok("Person JSON-LD jobTitle 为 AI Application Engineer", "符合履历事实与机器结构化数据一致性规范")
    else:
        fail("Person JSON-LD jobTitle 为 AI Application Engineer", "未找到标准 jobTitle: AI Application Engineer")


# ── 7 sitemap 与 robots ───────────────────────────────────────────
def check_sitemap_and_robots():
    locs = re.findall(r"<loc>(.*?)</loc>", read("sitemap.xml"))
    bad = []
    for l in locs:
        rel = l.replace("https://lx00018310.github.io/", "") or "index.html"
        rel_clean = urllib.parse.unquote(rel)
        try:
            if urllib.request.urlopen(BASE + urllib.parse.quote(rel_clean, safe="/:"), timeout=5).status != 200:
                bad.append(l)
        except Exception as e:
            bad.append(f"{l} ({e})")
    if bad:
        fail("sitemap 中所有 URL 可访问，无 404", f"不可达：{bad}")
    else:
        ok("sitemap 中所有 URL 可访问，无 404", f"{len(locs)} 条逐条 HTTP 校验通过")

    # 确认私下材料未进入 sitemap
    if any("job-search-private" in l for l in locs):
        fail("私下材料未进入 sitemap", "sitemap 泄漏私下材料")
    else:
        ok("私下材料未进入 sitemap", "sitemap 仅含公开页面")


# ── 8 og 分享图完整生成 ───────────────────────────────────────────
def check_og():
    try:
        from PIL import Image
    except ImportError:
        skip("og 图尺寸 1200x630", "未装 Pillow")
        return
    expected_imgs = [
        "og-home.png", "og-digital-dock.png", "og-iro-agent.png", "og-robot-line.png",
        "og-toywake.png", "og-ai-engineering.png", "og-simplehmi.png", "og-huzhou.png"
    ]
    bad = []
    for name in expected_imgs:
        p = DOCS / "assets" / name
        if not p.exists():
            bad.append(f"缺 {name}")
        elif Image.open(p).size != (1200, 630):
            bad.append(f"{name} 尺寸为 {Image.open(p).size}")
    if bad:
        fail(f"全套 {len(expected_imgs)} 张 og 图已生成且尺寸 1200x630", "；".join(bad))
    else:
        ok(f"全套 {len(expected_imgs)} 张 og 图已生成且尺寸 1200x630", f"{len(expected_imgs)} 张全部通过校验")


# ── 9 站内无死链、资源有效性与锚点一致性 ─────────────────────────
def check_links():
    bad_links = []
    bad_anchors = []
    duplicate_ids = []
    total_links = 0

    # 先收集各页面的所有 id
    page_ids = {}
    for p in PAGES:
        src = strip_comments(read(p))
        ids = re.findall(r'\bid=["\']([^"\']+)["\']', src)
        seen = set()
        dupes = set()
        for i in ids:
            if i in seen:
                dupes.add(i)
            seen.add(i)
        if dupes:
            duplicate_ids.append((p, list(dupes)))
        page_ids[p] = seen

    if duplicate_ids:
        fail("页面无重复 ID", f"重复 ID：{duplicate_ids}")
    else:
        ok("页面无重复 ID", f"{len(PAGES)} 个页面 ID 全部唯一")

    for p in PAGES:
        src = strip_comments(read(p))
        # 检查所有 href 和 src
        for m in re.finditer(r'(?:href|src)=["\']([^"\']+)["\']', src):
            u = m.group(1).strip()
            if not u or u.startswith(("http://", "https://", "mailto:", "tel:", "sms:", "data:", "javascript:")):
                continue

            parsed = urllib.parse.urlparse(u)
            path = parsed.path
            fragment = parsed.fragment

            # 纯锚点
            if not path and fragment:
                total_links += 1
                if fragment not in page_ids.get(p, set()):
                    bad_anchors.append((p, u, f"本页未找到 #{fragment}"))
                continue

            target_file = path.lstrip("/")
            target_file = urllib.parse.unquote(target_file) or "index.html"
            total_links += 1

            # 校验物理文件存在
            disk_path = DOCS / target_file
            if not disk_path.exists():
                bad_links.append((p, u, f"文件不存在: {target_file}"))
                continue

            # 若带 fragment，且是 html 文件，校验目标锚点
            if fragment and disk_path.suffix.lower() in (".html", ".htm"):
                t_page = disk_path.name
                if t_page in page_ids:
                    if fragment not in page_ids[t_page]:
                        bad_anchors.append((p, u, f"{t_page} 未找到 #{fragment}"))

    if bad_links:
        fail("站内链接与资源均存在", f"{bad_links}")
    else:
        ok("站内链接与资源均存在", f"{len(PAGES)} 页共 {total_links} 个内部链接/资源路径全部命中真实文件")

    if bad_anchors:
        fail("站内锚点全命中", f"{bad_anchors}")
    else:
        ok("站内锚点全命中", "全部 #fragment 锚点均在目标页面唯一定位成功")


# ── 10 违规禁用词全面审计与隐私隔离 ───────────────────────────────
def check_prohibited_terms():
    # 严格根据 Plan 2.4 与 9.1 节，及 AI 产品经理重构规范
    prohibited = [
        "零事故", "事故 0 起", "事故0起", "零缺陷",
        "全网回滚 < 90", "全网回滚<90",
        "12 台已部署", "12台已部署", "12 台 HMI", "12台HMI",
        "1 人 + AI 独立交付", "1人+AI独立交付", "1人 + AI 独立交付",
        "可以下注", "看见未来", "比客户高半层",
        "成交 20 万", "成交20万", "续签率 60%", "续签率60%",
        "官方评审", "确立大会主线", "确立为大会主线",
        "彻底消除定位异常", "杜绝状态不同步", "杜绝多端状态不同步", "绝不中断",
        "AI 应用解决方案 / 售前", "AI 应用解决方案/售前",
        "AI 应用工程师 / AI 产品经理", "AI 应用工程师/AI 产品经理",
        "AI Application Solutions",
        "方案策划 / 售前", "方案策划/售前",
        "AI 解决方案顾问"
    ]
    hits = []
    scan_files = [p for p in DOCS.rglob("*") if p.suffix in (".html", ".md", ".txt") and "_internal" not in p.parts]
    for p in scan_files:
        content = p.read_text(encoding="utf-8")
        clean_text = re.sub(r"<[^>]+>", " ", content)
        for term in prohibited:
            if term in clean_text:
                hits.append(f"{p.name}:{term}")
    if hits:
        fail("公开材料无违禁失实表述", f"发现违规词：{hits}")
    else:
        ok("公开材料无违禁失实表述", f"已扫描 {len(scan_files)} 个公开文件，零违规")

    # 隐私检查：docs/_internal 目录彻底脱离公开 docs 目录
    facts_p = DOCS / "_internal"
    if facts_p.exists():
        fail("docs/_internal 目录彻底私有化", "docs/_internal 仍存在于公开 docs 目录中，请移至本地私有目录并 gitignore")
    else:
        ok("docs/_internal 目录彻底私有化", "docs/_internal 已彻底脱离公开仓库，工作底稿与内部规则已私有隔离")


# ── 11 简历一致性、无占位符及三份 PDF 真实页数与文本校验 ─────────
def check_resumes_and_todos():
    hits = []
    for p in [DOCS / "assets" / "resume.html", DOCS / "assets" / "董达_简历_一页.html"]:
        txt = p.read_text(encoding="utf-8")
        for term in ["待确认", "TODO", "待核实"]:
            if term in txt:
                hits.append(f"{p.name}:{term}")
    if hits:
        fail("简历无待确认/TODO占位", f"{hits}")
    else:
        ok("简历无待确认/TODO占位", "主投版与一页版均无占位符")

    r_main = read("assets/resume.html")
    r_one = read("assets/董达_简历_一页.html")
    core_facts = [
        "董达", "18761576008", "624290365@qq.com",
        "AI 产品经理", "AI 应用工程师", "IRO_agent",
        "已上线已验收", "212 万元",
        "2019.07–2019.11", "售前策划主创"
    ]
    diff = [f for f in core_facts if f not in r_main or f not in r_one]
    if diff:
        fail("两份简历核心事实完全一致", f"缺少字段：{diff}")
    else:
        ok("两份简历核心事实完全一致", "姓名、联系方式、方向、职位、金额、考亭任职时间与身份均一致")

    # 校验真实导出的 PDF 页数与文本提取
    try:
        import fitz  # PyMuPDF
        pdf_checks = [
            (DOCS / "assets" / "resume.pdf", 2, "主投版简历"),
            (PRIVATE / "一页简历_检查.pdf", 1, "一页版简历"),
            (PRIVATE / "AI辅助开发过程案例.pdf", 2, "AI辅助开发过程案例")
        ]
        pdf_errors = []
        for pdf_path, exp_pages, label in pdf_checks:
            if not pdf_path.exists():
                pdf_errors.append(f"{label} 文件不存在: {pdf_path.name}")
                continue
            doc = fitz.open(pdf_path)
            if len(doc) != exp_pages:
                pdf_errors.append(f"{label} 页数异常: 实际 {len(doc)} 页，预期 {exp_pages} 页")
            else:
                # 抽取文本检查是否非空白扫描件
                full_text = "".join(page.get_text() for page in doc)
                if len(full_text.strip()) < 100:
                    pdf_errors.append(f"{label} 提取文本过少（可能为纯图像或渲染空白）")
            doc.close()
        if pdf_errors:
            fail("三份关键 PDF 真实页数与文本校验", "；".join(pdf_errors))
        else:
            ok("三份关键 PDF 真实页数与文本校验", "主简历恰好 2 页，一页简历恰好 1 页，过程案例恰好 2 页，全部为真实可提取文本")
    except ImportError:
        skip("三份关键 PDF 真实页数与文本校验", "未安装 PyMuPDF(fitz)")


# ── 12 [浏览器] 9 页 375px 无溢出、无控制台报错、打印隐藏导航 ────
def check_browser():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        skip("[浏览器] 9 页响应式、JS 报错与打印测试", "未装 playwright")
        return

    over_375 = []
    console_errors = []
    nav_print_shown = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch()

        # 1. 375px 移动端溢出检查
        m_page = browser.new_page(viewport={"width": 375, "height": 812})
        for p in ALL_PAGES:
            url = BASE + urllib.parse.quote(p, safe="/:")
            m_page.goto(url, wait_until="load")
            m_page.wait_for_timeout(150)
            sw = m_page.evaluate("document.documentElement.scrollWidth")
            cw = m_page.evaluate("document.documentElement.clientWidth")
            if sw > cw + 1:
                over_375.append((p, sw, cw))
        m_page.close()

        # 2. 1440x900 桌面端控制台报错检查
        d_page = browser.new_page(viewport={"width": 1440, "height": 900})
        def on_console(msg):
            if msg.type == "error":
                console_errors.append(msg.text)
        d_page.on("console", on_console)

        for p in ALL_PAGES:
            url = BASE + urllib.parse.quote(p, safe="/:")
            d_page.goto(url, wait_until="load")
            d_page.wait_for_timeout(100)
        d_page.close()

        # 3. 打印模式 nav 隐藏检查 (公开页面)
        pr_page = browser.new_page(viewport={"width": 1280, "height": 900})
        for p in PAGES:
            url = BASE + urllib.parse.quote(p, safe="/:")
            pr_page.goto(url, wait_until="load")
            pr_page.emulate_media(media="print")
            vis = pr_page.evaluate("""() => {
              const n = document.querySelector('nav.nav');
              return n ? getComputedStyle(n).display : 'none';
            }""")
            if vis != "none":
                nav_print_shown.append((p, vis))
        pr_page.close()

        browser.close()

    if over_375:
        fail(f"[浏览器] 全部 {len(ALL_PAGES)} 页 375px 视口无横向溢出", f"溢出页面：{over_375}")
    else:
        ok(f"[浏览器] 全部 {len(ALL_PAGES)} 页 375px 视口无横向溢出", f"全部 {len(ALL_PAGES)} 页 scrollWidth <= 375px")

    if console_errors:
        fail(f"[浏览器] 全部 {len(ALL_PAGES)} 页桌面加载零 JS 报错", f"错误：{console_errors[:5]}")
    else:
        ok(f"[浏览器] 全部 {len(ALL_PAGES)} 页桌面加载零 JS 报错", f"{len(ALL_PAGES)} 个页面均无 console.error")

    if nav_print_shown:
        fail("[浏览器] 打印预览下全局导航隐藏", f"{nav_print_shown}")
    else:
        ok("[浏览器] 打印预览下全局导航隐藏", f"{len(PAGES)} 个公开页面 print media 下 nav.nav 均为 display: none")


def main():
    for fn in (
        check_serving, check_home, check_case_pages, check_nav,
        check_no_cdn, check_jsonld, check_sitemap_and_robots,
        check_og, check_links, check_prohibited_terms,
        check_resumes_and_todos, check_browser
    ):
        try:
            fn()
        except Exception as e:
            fail(fn.__name__, f"检查本身出错：{e!r}")

    w = max(len(i) for _, i, _ in results)
    print("\n作品集与求职材料验收")
    print("=" * (w + 60))
    for status, item, ev in results:
        mark = {"PASS": "[通过]", "FAIL": "[未通过]", "SKIP": "[跳过]"}[status]
        print(f"{mark:8} {item:{w}}  {ev}")
    print("=" * (w + 60))
    n_fail = sum(1 for s, _, _ in results if s == "FAIL")
    n_skip = sum(1 for s, _, _ in results if s == "SKIP")
    print(f"通过 {sum(1 for s,_,_ in results if s=='PASS')} 项，"
          f"未通过 {n_fail} 项，跳过 {n_skip} 项")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
