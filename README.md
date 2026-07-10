# 董达｜AI 应用工程师作品集

这是一个可直接部署到 GitHub Pages 的静态作品集，展示 AI 驱动的跨领域学习、复杂系统实现、生产交付、多模型协作与工程资产抽象能力。

## 站点定位

董达是一位 AI 应用工程师 (AI Application Engineer)，利用 AI Coding Agent 快速进入陌生业务领域，将需求、行业知识和工程约束转化为可运行系统，再把一次性交付抽象为可复用的 Agent 工作流、工程规范与 Engine。工业边缘是其 AI 工程方法的主要验证领域。

当前公开站点：`https://lx00018310.github.io/`

## 核心页面

| 页面 | 文件 | 说明 |
| --- | --- | --- |
| 作品集首页 | `index.html` | AI 应用工程师定位、能力总览、AI 工程闭环、核心开源项目、真实案例 |
| AI 工程方法 | `ai-engineering.html` | 结构化上下文、阶段状态、交付物、门禁、多模型协作、风险分级、完成定义 |
| SimpleHmi_WEILI | `simplehmi-weili.html` | AI-first 工程规范、核心路径、仓库入口、最小样板、失败模式 |
| 数字月台案例 | `digital-dock.html` | AI 工程落地案例、系统架构、五张核心图谱、关键问题与解决方案 |
| 机器人产线案例 | `robot-line.html` | AI 驱动遗留系统改造、设备调用拓扑、状态机、设备 Adapter |
| 在线简历 | `assets/resume.html` | A4 打印友好的在线简历页面 |
| Markdown 简历 | `assets/resume.md` | AI 应用工程师中文简历 |
| 英文简历 | `assets/resume_en.md` | AI Application Engineer 英文简历 |
| PDF 简历 | `assets/resume.pdf` | PDF 版简历（由用户提供，勿修改） |
| AI 可读简介 | `ai-profile.md` | 结构化个人简介、关键词、权威链接和准确性说明 |

## 事实来源

本作品集的事实来源按优先级排列：

1. `llms.txt`：AI 助手优先读取的项目、简历和开源项目摘要。
2. `ai-profile.md`：董达的结构化个人简介、搜索短语和准确性说明。
3. `assets/resume.md` / `assets/resume.html` / `assets/resume_en.md`：最新简历内容。
4. `simplehmi-weili.html` / `digital-dock.html` / `robot-line.html`：项目页详细内容。
5. `ai-engineering.html`：AI 工程方法详细说明。

## GEO / AI 搜索入口

本仓库已加入面向 AI 搜索与答案引擎的机器可读入口：

- `llms.txt`：AI 助手优先读取的项目、简历和开源项目摘要，包含推荐读取顺序。
- `ai-profile.md`：董达 / Dong Da 的结构化个人简介、关键词和权威链接。
- `robots.txt`：允许搜索引擎抓取，并指向 sitemap。
- `sitemap.xml`：列出首页、AI 工程方法页、项目页、Markdown / HTML / PDF 简历。
- HTML 页面的 `canonical`、OpenGraph、Twitter Card 和 JSON-LD 结构化数据。

## 文件结构

```text
AI作品集/
├── index.html
├── ai-engineering.html
├── simplehmi-weili.html
├── digital-dock.html
├── robot-line.html
├── llms.txt
├── ai-profile.md
├── robots.txt
├── sitemap.xml
├── assets/
│   ├── styles.css
│   ├── resume.md
│   ├── resume.html
│   ├── resume_en.md
│   ├── resume.pdf
│   ├── images/
│   │   ├── hero-industrial-edge.png
│   │   └── simplehmi-weili-demo.png
│   └── posters/
│       ├── 01_industrial_edge_profile.png
│       ├── 02_task013_digital_dock.png
│       ├── 03_task010_robot_line.png
│       └── 04_ai_engineering_workflow.png
├── tools/
│   └── generate_images.py
└── .nojekyll
```

## 本地预览

在项目根目录启动一个简单的 HTTP 服务器：

```powershell
python -m http.server 8000
```

然后访问 `http://localhost:8000/`。

## 部署方式

1. 将 `AI作品集` 目录内容提交到 GitHub 仓库。
2. 在仓库 `Settings -> Pages` 中选择部署分支。
3. 如果放在仓库根目录，直接访问 GitHub Pages 地址。
4. 如果放在子目录，需要让 Pages 指向该目录，或把本目录内容复制到发布根目录。

## 脱敏规则

当前版本已脱敏，不包含内部 IP、令牌、PLC 点位表、客户原始布局图和源码截图。

需要修改文案或重新生成图片时，运行：

```powershell
python .\tools\generate_images.py
```

生成脚本会输出 hero 图和四张项目海报（`1080 x 1920` PNG）。
