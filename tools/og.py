#!/usr/bin/env python3
"""社交预览图生成器：把 tools/og.html 里每个 .og 元素截成 1200x630 的 PNG。

用法：
    python tools/og.py

新增一张图不用改这个脚本 —— 在 og.html 里加一个 <div class="og" id="og-xxx">
就行，输出文件名取自 id。

依赖：playwright（pip install playwright && playwright install chromium）。
没有 playwright 时脚本直接报错退出，不会悄悄跳过 —— 不许假成功。
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "og.html"
OUT = ROOT / "docs" / "assets"

SIZE = (1200, 630)


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("缺少 playwright。先执行：pip install playwright && playwright install chromium",
              file=sys.stderr)
        return 1

    if not SRC.exists():
        print(f"找不到 {SRC}", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 900},
                                device_scale_factor=1)
        page.goto(SRC.as_uri())
        page.wait_for_timeout(400)  # 等字体落位

        ids = page.eval_on_selector_all(".og", "els => els.map(e => e.id)")
        if not ids:
            print("og.html 里没有 .og 元素", file=sys.stderr)
            browser.close()
            return 1

        failed = []
        for el_id in ids:
            box = page.locator("#" + el_id).bounding_box()
            if not box or round(box["width"]) != SIZE[0] or round(box["height"]) != SIZE[1]:
                failed.append(f"{el_id} 尺寸是 {box and (box['width'], box['height'])}，"
                              f"不是 {SIZE[0]}x{SIZE[1]}")
                continue
            dest = OUT / f"{el_id}.png"
            page.locator("#" + el_id).screenshot(path=str(dest))
            print(f"  写入 {dest.relative_to(ROOT)}  {SIZE[0]}x{SIZE[1]}")

        browser.close()

    if failed:
        print("\n以下元素尺寸不对，未生成：", file=sys.stderr)
        for f in failed:
            print("  " + f, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
