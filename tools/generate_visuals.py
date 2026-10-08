"""生成定稿首页使用的中英文数字月台拓扑图。"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets" / "visuals"

COPY = {
    "zh": [
        "数字月台：PLC 与移动机器人联控", "用一套统一的状态逻辑，把设备动作管起来",
        "移动机器人", "导航与动作协同", "接入统一状态逻辑",
        "多设备与断线", "设备状态协同", "连接中断与异常处理",
        "本人负责：工控软件系统", "中控核心服务 (Fastify)",
        "统一状态机管理设备动作", "协调多设备与断线状态", "状态：上线通过验收",
        "WebSocket", "HMI 界面 (React + TS)", "设备状态呈现 / 现场操作", "中控状态同步",
        "现场 PLC", "设备控制信号", "接入统一状态逻辑",
        "系统关系示意｜PLC 与移动机器人接入统一状态逻辑，真机联调，上线通过验收",
    ],
    "en": [
        "Digital Loading Dock: PLCs & Mobile Robots", "Unified state logic orchestrates device actions",
        "Mobile Robots", "Navigation & actions", "Unified state logic",
        "Scale & Dropouts", "Device coordination", "Disconnect handling",
        "Control Software", "Core Service (Fastify)",
        "Unified state machine", "Device & connection states", "Passed final acceptance",
        "WebSocket", "HMI (React + TS)", "Device states / operations", "Control state updates",
        "On-site PLCs", "Device control signals", "Unified state logic",
        "Topology overview | PLCs & mobile robots connected, commissioned on live hardware, accepted",
    ],
}


def generate(language):
    c = COPY[language]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 400" width="100%" height="100%" role="img" aria-label="' + escape(c[0], quote=True) + '">',
             '<rect width="720" height="400" fill="#FAFCFD" rx="14"/>',
             '<rect x="12" y="12" width="696" height="376" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>']

    def text(x, y, value, size=11, color="#475569", bold=False):
        parts.append(f'<text x="{x}" y="{y}" font-family="Microsoft YaHei, Arial, sans-serif" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}">{escape(value)}</text>')

    def box(x, y, w, h, fill="#FAF5FF", stroke="#CBD5E1"):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}"/>')

    text(28, 42, c[0], 16, "#0F172A", True)
    text(28, 62, c[1], 12)
    for y, offset in [(92, 2), (218, 5)]:
        box(36, y, 170, 96)
        text(52, y + 28, c[offset], 13, "#0F172A", True)
        text(52, y + 52, c[offset + 1])
        text(52, y + 76, c[offset + 2])
    box(236, 84, 268, 240, "#FDF4FF", "#D946EF")
    box(236, 84, 268, 32, "#D946EF", "#D946EF")
    text(252, 105, c[8], 12, "#FFFFFF", True)
    box(252, 128, 236, 88, "#FFFFFF", "#F5D0FE")
    for y, i in [(152, 9), (173, 10), (191, 11), (207, 12)]:
        text(264, y, c[i], 12 if i == 9 else 11, "#D946EF" if i == 9 else "#475569", i == 9)
    parts.append('<path d="M 370 220 L 370 237" stroke="#D946EF" stroke-width="2"/>')
    text(382, 233, c[13], 10, "#D946EF")
    box(252, 240, 236, 72, "#FFFFFF", "#F5D0FE")
    text(264, 262, c[14], 13, "#0F172A", True)
    text(264, 282, c[15])
    text(264, 300, c[16])
    box(534, 150, 156, 110)
    text(548, 178, c[17], 13, "#0F172A", True)
    text(548, 204, c[18])
    text(548, 230, c[19])
    for x1, x2, y in [(206, 236, 140), (206, 236, 266), (504, 534, 205)]:
        parts.append(f'<path d="M {x1} {y} L {x2} {y}" stroke="#D946EF" stroke-width="2"/>')
        parts.append(f'<polygon points="{x2},{y} {x2-8},{y-4} {x2-8},{y+4}" fill="#D946EF"/>')
        parts.append(f'<polygon points="{x1},{y} {x1+8},{y-4} {x1+8},{y+4}" fill="#D946EF"/>')
    box(28, 344, 664, 30)
    text(40, 363, c[20], 10)
    parts.append('</svg>')
    dest = OUT / ("dock-system.svg" if language == "zh" else "dock-system-en.svg")
    dest.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"Generated {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    generate("zh")
    generate("en")
