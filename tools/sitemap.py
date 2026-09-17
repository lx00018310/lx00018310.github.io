#!/usr/bin/env python3
"""从 docs/ 实际存在的文件生成 sitemap.xml。

为什么用脚本而不是手写：手写的 sitemap 会随着改名慢慢烂掉，而验收清单要求
「sitemap 中所有 URL 可访问，无 404」。这里以磁盘为准，文件不存在就不会被写进去。

用法：python tools/sitemap.py
"""
import sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://lx00018310.github.io/"

# 路径 -> (changefreq, priority)。顺序即 sitemap 里的顺序。
ENTRIES = [
    ("index.html",            "weekly",  "1.0"),
    ("digital-dock.html",     "monthly", "0.9"),
    ("iro-agent.html",        "monthly", "0.9"),
    ("robot-line.html",       "monthly", "0.8"),
    ("toywake.html",          "monthly", "0.8"),
    ("ai-engineering.html",   "monthly", "0.8"),
    ("simplehmi-weili.html",  "monthly", "0.8"),
    ("huzhou-food-map.html",  "monthly", "0.6"),
    ("assets/董达_简历_一页.html", "monthly", "0.9"),
    ("assets/resume.html",    "monthly", "0.8"),
    ("ai-profile.md",         "monthly", "0.5"),
]

# 不许进 sitemap 的东西（内部草稿、验证文件）
EXCLUDE_PREFIX = ("_internal/",)


def main() -> int:
    missing = [p for p, _, _ in ENTRIES if not (DOCS / p).exists()]
    if missing:
        print("以下文件不存在，拒绝生成 sitemap（不发 404）：", file=sys.stderr)
        for m in missing:
            print("  " + m, file=sys.stderr)
        return 1

    bad = [p for p, _, _ in ENTRIES if p.startswith(EXCLUDE_PREFIX)]
    if bad:
        print(f"内部路径不许进 sitemap: {bad}", file=sys.stderr)
        return 1

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             "<!-- 由 tools/sitemap.py 生成，不要手改。改完页面重新跑一次脚本。 -->",
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', ""]
    for path, freq, prio in ENTRIES:
        mtime = datetime.fromtimestamp((DOCS / path).stat().st_mtime, timezone.utc)
        # 非 ASCII 路径必须百分号编码，否则 sitemap 不合法
        safe = quote(path, safe="/._-")
        loc = SITE if path == "index.html" else SITE + safe
        lines += ["  <url>",
                  f"    <loc>{loc}</loc>",
                  f"    <lastmod>{mtime:%Y-%m-%d}</lastmod>",
                  f"    <changefreq>{freq}</changefreq>",
                  f"    <priority>{prio}</priority>",
                  "  </url>", ""]
    lines.append("</urlset>")

    out = DOCS / "sitemap.xml"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"写入 {out.relative_to(ROOT)}，{len(ENTRIES)} 条 URL，全部已确认文件存在。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
