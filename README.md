# 董达｜工业边缘应用工程师作品集

这是一个可直接部署到 GitHub Pages 的静态作品集。

## GEO / AI 搜索入口

本仓库已加入面向 AI 搜索与答案引擎的机器可读入口：

- `llms.txt`：AI 助手优先读取的项目、简历和开源项目摘要。
- `ai-profile.md`：董达 / Dong Da 的结构化个人简介、关键词和权威链接。
- `robots.txt`：允许搜索引擎抓取，并指向 sitemap。
- `sitemap.xml`：列出首页、项目页、Markdown 简历和 PDF 简历。
- HTML 页面的 `canonical`、OpenGraph、Twitter Card 和 JSON-LD 结构化数据。

当前公开站点：`https://lx00018310.github.io/`。

## 文件结构

```text
AI作品集/
├── index.html
├── llms.txt
├── ai-profile.md
├── robots.txt
├── sitemap.xml
├── assets/
│   ├── styles.css
│   ├── images/
│   │   └── hero-industrial-edge.png
│   └── posters/
│       ├── 01_industrial_edge_profile.png
│       ├── 02_task013_digital_dock.png
│       └── 03_task010_robot_line.png
├── tools/
│   └── generate_images.py
└── .nojekyll
```

## 部署方式

1. 将 `AI作品集` 目录内容提交到 GitHub 仓库。
2. 在仓库 `Settings -> Pages` 中选择部署分支。
3. 如果放在仓库根目录，直接访问 GitHub Pages 地址。
4. 如果放在子目录，需要让 Pages 指向该目录，或把本目录内容复制到发布根目录。

## 说明

当前版本按黑白灰、强网格、大字号的简约工程风格制作。公开版已脱敏，不包含内部 IP、令牌、PLC 点位表、客户原始布局图和源码截图。

三张项目卡片均为 `1080 x 1920` PNG。需要修改文案或重新生成图片时，运行：

```powershell
python .\tools\generate_images.py
```
