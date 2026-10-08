"""当前作品集的图片生成入口：从 tools/og.html 生成首页分享图。

实景与项目截图沿用定稿首页已有素材；不再生成旧版海报和案例图片。
用法：python -X utf8 tools/generate_images.py
"""
import sys
from og import main

if __name__ == "__main__":
    sys.exit(main())
