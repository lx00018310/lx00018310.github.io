from __future__ import annotations

from pathlib import Path
from typing import Sequence

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "docs" / "assets" / "images"
POSTER_DIR = ROOT / "docs" / "assets" / "posters"

FONT_REG = Path(r"C:\Windows\Fonts\msyh.ttc")
FONT_BOLD = Path(r"C:\Windows\Fonts\msyhbd.ttc")

BLACK = "#000000"
WHITE = "#ffffff"
PAPER = "#f4f4f1"
LIGHT = "#e2e2de"
MID = "#767676"
DARK = "#1d1d1d"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)


def text_box(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, face: ImageFont.ImageFont, width: int, fill: str = BLACK, gap: int = 10) -> int:
    x, y = xy
    line = ""
    lines: list[str] = []
    for ch in text:
        trial = line + ch
        if ch == "\n":
            lines.append(line)
            line = ""
        elif draw.textlength(trial, font=face) <= width or not line or ch in "。，、；：！？,.!?;:":
            line = trial
        else:
            lines.append(line)
            line = ch
    if line:
        lines.append(line)
    offset = 0
    for item in lines:
        draw.text((x, y + offset), item, font=face, fill=fill)
        bbox = draw.textbbox((x, y + offset), item or " ", font=face)
        offset += bbox[3] - bbox[1] + gap
    return offset


def rule(draw: ImageDraw.ImageDraw, y: int, x1: int = 64, x2: int = 1016, w: int = 3) -> None:
    draw.line((x1, y, x2, y), fill=BLACK, width=w)


def rect(draw: ImageDraw.ImageDraw, box: Sequence[int], fill: str = WHITE, outline: str = BLACK, w: int = 3) -> None:
    draw.rectangle(tuple(box), fill=fill, outline=outline, width=w)


def label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, inverse: bool = True) -> None:
    x, y = xy
    face = font(25, True)
    bbox = draw.textbbox((0, 0), text, font=face)
    pad_x, pad_y = 14, 8
    box = (x, y, x + bbox[2] - bbox[0] + pad_x * 2, y + bbox[3] - bbox[1] + pad_y * 2)
    draw.rectangle(box, fill=BLACK if inverse else WHITE, outline=BLACK, width=2)
    draw.text((x + pad_x, y + pad_y - 2), text, font=face, fill=WHITE if inverse else BLACK)


def footer(draw: ImageDraw.ImageDraw) -> None:
    rule(draw, 1846, w=2)
    draw.text((64, 1874), "董达｜AI 应用工程师｜电话 / 微信：18761576008", font=font(24), fill=BLACK)
    draw.text((1016, 1874), "PUBLIC PORTFOLIO", font=font(20, True), fill=MID, anchor="ra")


def draw_header(draw: ImageDraw.ImageDraw, tag: str, title: str, sub: str) -> None:
    label(draw, (64, 58), tag)
    text_box(draw, (64, 132), title, font(64, True), 940, BLACK, gap=12)
    rule(draw, 292)
    text_box(draw, (64, 320), sub, font(28), 900, DARK, gap=8)


def metric_row(draw: ImageDraw.ImageDraw, y: int, items: list[tuple[str, str]]) -> None:
    gap = 16
    x = 64
    w = (952 - gap * (len(items) - 1)) // len(items)
    for name, value in items:
        rect(draw, (x, y, x + w, y + 128), WHITE, BLACK, 2)
        draw.text((x + 18, y + 18), name, font=font(22, True), fill=MID)
        draw.text((x + 18, y + 60), value, font=font(38, True), fill=BLACK)
        x += w + gap


def process_band(draw: ImageDraw.ImageDraw, y: int, steps: list[str], h: int = 112) -> None:
    x = 64
    gap = 10
    w = (952 - gap * (len(steps) - 1)) // len(steps)
    for idx, step in enumerate(steps):
        fill = BLACK if idx == 0 else WHITE
        fg = WHITE if idx == 0 else BLACK
        rect(draw, (x, y, x + w, y + h), fill, BLACK, 3)
        text_box(draw, (x + 14, y + 22), step, font(24, True), w - 28, fg, gap=4)
        if idx < len(steps) - 1:
            draw.line((x + w, y + h // 2, x + w + gap, y + h // 2), fill=BLACK, width=3)
        x += w + gap


def three_columns(draw: ImageDraw.ImageDraw, y: int, items: list[tuple[str, str]], h: int = 250) -> None:
    gap = 16
    x = 64
    w = (952 - gap * 2) // 3
    for title, body in items:
        rect(draw, (x, y, x + w, y + h), WHITE, BLACK, 3)
        draw.text((x + 18, y + 18), title, font=font(31, True), fill=BLACK)
        text_box(draw, (x + 18, y + 76), body, font(23), w - 36, DARK, gap=8)
        x += w + gap


def poster_profile() -> None:
    im = Image.new("RGB", (1080, 1920), PAPER)
    draw = ImageDraw.Draw(im)
    for x in range(64, 1017, 119):
        draw.line((x, 0, x, 1920), fill=LIGHT, width=1)

    draw_header(
        draw,
        "PROFILE 01",
        "AI\n应用工程师",
        "利用 AI Coding Agent 快速进入陌生领域，把需求、行业知识和工程约束转化为可运行系统，再沉淀为 Agent 工作流与工程规范。",
    )
    metric_row(draw, 448, [("经验", "16 年"), ("方式", "AI 驱动"), ("目标", "可交付")])

    draw.text((64, 664), "能力结构", font=font(44, True), fill=BLACK)
    rule(draw, 726)
    rows = [
        ("01", "陌生领域进入", "用 AI 阅读文档、源码、协议，输出领域模型与接口拓扑。"),
        ("02", "复杂系统实现", "AI Coding 贯通前后端、设备接入、状态机与部署。"),
        ("03", "Agent 工作流", "上下文、读取顺序、阶段状态、交付物与门禁。"),
        ("04", "系统集成", "API、设备、遗留系统接入，处理协议与并发冲突。"),
        ("05", "工程资产沉淀", "规范、模板、Skills、Adapters、检查清单与多模型审查。"),
    ]
    y = 760
    for no, title, body in rows:
        draw.text((64, y), no, font=font(42, True), fill=BLACK)
        draw.text((156, y + 4), title, font=font(32, True), fill=BLACK)
        text_box(draw, (434, y + 8), body, font(24), 560, DARK, gap=6)
        draw.line((64, y + 78, 1016, y + 78), fill=LIGHT, width=2)
        y += 102

    draw.text((64, 1330), "项目证据", font=font(44, True), fill=BLACK)
    rule(draw, 1392)
    three_columns(
        draw,
        1432,
        [
            ("SimpleHmi_WEILI", "AI-first 工程规范：约束 AI 生成可运行、可部署、可验收的工业系统。"),
            ("数字月台", "AI 工程落地：12 台 HMI + PLC + 调度 + 人脸 + 发布控制。"),
            ("机器人产线", "AI 驱动改造：遗留系统阅读、调用拓扑、状态机与设备 Adapter。"),
        ],
        h=286,
    )
    footer(draw)
    im.save(POSTER_DIR / "01_industrial_edge_profile.png", quality=95)


def poster_task013() -> None:
    im = Image.new("RGB", (1080, 1920), WHITE)
    draw = ImageDraw.Draw(im)
    for y in range(0, 1920, 120):
        draw.line((0, y, 1080, y), fill=LIGHT, width=1)

    draw_header(
        draw,
        "CASE 01",
        "数字月台\n12 台 HMI 协同系统",
        "公共工控机连接 HMI、PLC、调度系统、人脸设备和局域网发布链路。",
    )

    draw.text((64, 466), "系统结构", font=font(44, True), fill=BLACK)
    rule(draw, 528)
    rect(draw, (64, 586, 296, 1010), WHITE, BLACK, 3)
    for i, item in enumerate(["调度系统", "SLMP PLC", "人脸设备", "扫码与工位"]):
        yy = 620 + i * 92
        draw.text((92, yy), item, font=font(27, True), fill=BLACK)
        draw.line((92, yy + 46, 268, yy + 46), fill=LIGHT, width=2)
    draw.line((296, 796, 374, 796), fill=BLACK, width=5)

    rect(draw, (374, 620, 706, 972), BLACK, BLACK, 3)
    draw.text((540, 678), "公共工控机", font=font(40, True), fill=WHITE, anchor="ma")
    for i, item in enumerate(["Node / Fastify", "WebSocket 事件总线", "PostgreSQL 状态持久化", "部署控制器 / HMI Agent"]):
        draw.text((540, 748 + i * 45), item, font=font(23), fill=WHITE, anchor="ma")
    draw.line((706, 796, 784, 796), fill=BLACK, width=5)

    x0, y0 = 800, 592
    for i in range(12):
        col = i % 3
        row = i // 3
        x = x0 + col * 70
        y = y0 + row * 92
        rect(draw, (x, y, x + 48, y + 62), WHITE, BLACK, 3)
        draw.text((x + 24, y + 18), f"{i+1:02d}", font=font(19, True), fill=BLACK, anchor="ma")
    draw.text((868, 972), "HMI 01-12", font=font(28, True), fill=BLACK, anchor="ma")

    draw.text((64, 1134), "核心贡献", font=font(44, True), fill=BLACK)
    rule(draw, 1196)
    items = [
        ("多终端交互", "登录确认、作业信息、设备控制、报警、管理调试与权限显隐。"),
        ("真实设备链路", "PLC 网关、调度 Adapter、人脸 ISUP 服务、事件推送和来源校验。"),
        ("部署控制", ".wrelease 发布包、12 节点准备/激活、失败回滚和离线恢复。"),
        ("生产边界", "生产环境拒绝 Mock 假成功，关键配置缺失时阻断启动或发布。"),
    ]
    y = 1236
    for idx, (title, body) in enumerate(items, start=1):
        draw.text((64, y), f"{idx:02d}", font=font(34, True), fill=BLACK)
        draw.text((142, y + 2), title, font=font(28, True), fill=BLACK)
        text_box(draw, (382, y + 4), body, font(22), 610, DARK, gap=6)
        draw.line((64, y + 72, 1016, y + 72), fill=LIGHT, width=2)
        y += 92

    rect(draw, (64, 1632, 1016, 1814), BLACK, BLACK, 3)
    draw.text((92, 1662), "当前结果", font=font(34, True), fill=WHITE)
    text_box(
        draw,
        (92, 1718),
        "主要软件链路、本机集成验证、PLC 业务状态聚合、人脸真实链路 MVP、HMI 局域网版本控制和部署自愈机制已形成。",
        font(24),
        880,
        WHITE,
        gap=8,
    )
    footer(draw)
    im.save(POSTER_DIR / "02_task013_digital_dock.png", quality=95)


def poster_task010() -> None:
    im = Image.new("RGB", (1080, 1920), PAPER)
    draw = ImageDraw.Draw(im)
    for x in range(64, 1017, 136):
        draw.line((x, 0, x, 1920), fill=LIGHT, width=1)

    draw_header(
        draw,
        "CASE 02",
        "自动化餐饮产线\n与送餐机器人",
        "工控机后端串联刷卡、选味、PLC、喷码、产线状态和机器人取送餐流程。",
    )

    draw.text((64, 464), "流程闭环", font=font(44, True), fill=BLACK)
    rule(draw, 526)
    process_band(draw, 584, ["刷卡器", "选味屏", "后端\n状态机", "PLC\n喷码", "机器人\n取送餐"], h=150)
    rect(draw, (64, 812, 1016, 1010), BLACK, BLACK, 3)
    text_box(
        draw,
        (94, 858),
        "刷卡 -> 选味 -> 投桶 -> PLC 确认 -> 喷码 -> 机器人取餐 -> 送餐 -> 返程",
        font(31, True),
        888,
        WHITE,
        gap=8,
    )
    text_box(draw, (94, 932), "重点不是单个页面，而是把现场流程和多设备状态变成可追踪、可复位、可部署的系统。", font(23), 888, WHITE, gap=8)

    draw.text((64, 1134), "关键工程处理", font=font(44, True), fill=BLACK)
    rule(draw, 1196)
    rows = [
        ("01", "读卡服务独占", "避免多个页面或进程竞争串口 / HID 设备。"),
        ("02", "机器人 API 卡顿", "串行任务、异步导航轮询、状态缓存和 Kiosk 降级隔离。"),
        ("03", "路线与地图恢复", "地图自动加载、路径点配置、环境预检和异常处理。"),
        ("04", "生产配置收敛", "dev / prod 分离，统一配置文件读取关键设备参数。"),
    ]
    y = 1240
    for no, title, body in rows:
        draw.text((64, y), no, font=font(34, True), fill=BLACK)
        draw.text((142, y + 2), title, font=font(28, True), fill=BLACK)
        text_box(draw, (418, y + 4), body, font(22), 560, DARK, gap=6)
        draw.line((64, y + 72, 1016, y + 72), fill=LIGHT, width=2)
        y += 94

    rect(draw, (64, 1648, 1016, 1814), WHITE, BLACK, 3)
    draw.text((92, 1682), "可迁移价值", font=font(34, True), fill=BLACK)
    text_box(draw, (92, 1736), "服务机器人、智能门店、展陈自动化、设备联动控制和现场调试平台。", font(25), 860, DARK, gap=8)
    footer(draw)
    im.save(POSTER_DIR / "03_task010_robot_line.png", quality=95)


def hero_image() -> None:
    im = Image.new("RGB", (2400, 1350), WHITE)
    draw = ImageDraw.Draw(im)
    for x in range(120, 2281, 120):
        draw.line((x, 0, x, 1350), fill=LIGHT, width=1)
    for y in range(90, 1261, 90):
        draw.line((0, y, 2400, y), fill=LIGHT, width=1)

    draw.text((120, 120), "AI APPLICATION", font=font(72, True), fill=BLACK)
    draw.text((120, 222), "ENGINEER", font=font(72, True), fill=BLACK)
    draw.line((120, 340, 2280, 340), fill=BLACK, width=6)

    rect(draw, (860, 470, 1540, 852), BLACK, BLACK, 5)
    draw.text((1200, 548), "AI 工程闭环", font=font(68, True), fill=WHITE, anchor="ma")
    draw.text((1200, 644), "陌生领域 → 领域抽象 → 系统实现 → 工程资产", font=font(34), fill=WHITE, anchor="ma")

    left = ["调度系统", "PLC / 点位 / 联锁", "人脸识别 / 扫码", "读卡 / 喷码 / 机器人"]
    for i, item in enumerate(left):
        y = 470 + i * 96
        rect(draw, (120, y, 520, y + 68), WHITE, BLACK, 4)
        draw.text((148, y + 16), item, font=font(32, True), fill=BLACK)
        draw.line((520, y + 34, 835, 660), fill=BLACK, width=4)

    for i in range(12):
        col = i % 4
        row = i // 4
        x = 1790 + col * 112
        y = 470 + row * 126
        rect(draw, (x, y, x + 76, y + 96), WHITE, BLACK, 4)
        draw.text((x + 38, y + 34), f"{i+1:02d}", font=font(26, True), fill=BLACK, anchor="ma")
    draw.line((1540, 660, 1760, 590), fill=BLACK, width=4)
    draw.line((1540, 660, 1760, 720), fill=BLACK, width=4)

    draw.text((120, 1132), "PUBLIC PORTFOLIO VISUAL / SANITIZED", font=font(30, True), fill=MID)
    draw.text((120, 1190), "董达｜AI 应用工程师", font=font(42, True), fill=BLACK)
    im.save(IMG_DIR / "hero-industrial-edge.png", quality=94)


def poster_ai_workflow() -> None:
    im = Image.new("RGB", (1080, 1920), WHITE)
    draw = ImageDraw.Draw(im)
    for y in range(0, 1920, 96):
        draw.line((0, y, 1080, y), fill=LIGHT, width=1)

    draw_header(
        draw,
        "WORKFLOW 04",
        "AI 工程闭环\n从陌生需求到可复用 Engine",
        "通过结构化上下文、阶段状态、交付物和门禁，把 AI 从代码生成器变成可控的工程协作者。",
    )

    draw.text((64, 466), "六阶段闭环", font=font(44, True), fill=BLACK)
    rule(draw, 528)
    steps = [
        ("01", "Context Intake", "读取业务文档、协议、源码、设备资料和现场约束"),
        ("02", "Domain Extraction", "形成领域对象、状态机、接口关系和风险边界"),
        ("03", "Plan & Architecture", "先规划再编码，明确范围、模块、数据流和验收标准"),
        ("04", "AI-assisted Build", "AI Coding Agent 完成实现，人负责关键判断与边界控制"),
        ("05", "Review & Verification", "多模型独立审查、自动化测试、真实链路验证和生产门禁"),
        ("06", "Abstraction & Handover", "沉淀为 Skills、Engine、规范、模板、SOP 和可维护文档"),
    ]
    y = 580
    for no, title, body in steps:
        draw.text((64, y), no, font=font(38, True), fill=BLACK)
        draw.text((148, y + 2), title, font=font(30, True), fill=BLACK)
        text_box(draw, (148, y + 42), body, font(22), 840, DARK, gap=4)
        draw.line((64, y + 86, 1016, y + 86), fill=LIGHT, width=2)
        y += 100

    draw.text((64, 1200), "AI 与人的职责分工", font=font(44, True), fill=BLACK)
    rule(draw, 1262)
    two_col_y = 1300
    rect(draw, (64, two_col_y, 520, two_col_y + 220), WHITE, BLACK, 3)
    draw.text((92, two_col_y + 18), "AI 的职责", font=font(30, True), fill=BLACK)
    text_box(draw, (92, two_col_y + 64), "搜索、理解、生成、审查、文档整理。在明确边界内提高执行效率，不替代人对方向和风险的判断。", font(23), 410, DARK, gap=8)
    rect(draw, (560, two_col_y, 1016, two_col_y + 220), BLACK, BLACK, 3)
    draw.text((588, two_col_y + 18), "人的职责", font=font(30, True), fill=WHITE)
    text_box(draw, (588, two_col_y + 64), "目标、边界、架构、风险、验收和最终责任。决定做什么、不做什么、做到什么程度，并对结果承担责任。", font(23), 410, WHITE, gap=8)

    rect(draw, (64, 1560, 1016, 1814), BLACK, BLACK, 3)
    draw.text((92, 1590), "核心原则", font=font(34, True), fill=WHITE)
    text_box(
        draw,
        (92, 1646),
        "AI 可以判断错，但工程流程不能失控。每一次交付可追踪、可审查、可复用。",
        font(24),
        880,
        WHITE,
        gap=8,
    )
    footer(draw)
    im.save(POSTER_DIR / "04_ai_engineering_workflow.png", quality=95)


def main() -> None:
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    POSTER_DIR.mkdir(parents=True, exist_ok=True)
    hero_image()
    poster_profile()
    poster_task013()
    poster_task010()
    poster_ai_workflow()


if __name__ == "__main__":
    main()
