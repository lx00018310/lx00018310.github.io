# 董达｜AI 应用工程师作品集

本仓库是董达的 AI 应用工程师个人作品集，是一个可直接部署到 GitHub Pages 的静态站点，展示 AI 驱动的跨领域学习、复杂系统实现、生产交付、多模型协作与工程资产抽象能力。

工业边缘、HMI、PLC、机器人和智能设备，是当前作品集中最主要的高约束工程验证场景，但网站的第一职业定位是 AI 应用工程师。

## 站点定位

董达是一位 AI 应用工程师 (AI Application Engineer)，利用 AI Coding Agent 快速进入陌生业务领域，将需求、行业知识和工程约束转化为可运行系统，再把一次性交付抽象为可复用的 Agent 工作流、工程规范与 Engine。工业边缘是其 AI 工程方法的主要验证领域。

当前公开站点：`https://lx00018310.github.io/`

## 核心页面

| 页面 | 文件 | 说明 |
| --- | --- | --- |
| 作品集首页 | `docs/index.html` | AI 应用工程师定位、能力总览、AI 工程闭环、核心开源项目、真实案例 |
| AI 工程方法 | `docs/ai-engineering.html` | 结构化上下文、阶段状态、交付物、门禁、多模型协作、风险分级、完成定义 |
| SimpleHmi_WEILI | `docs/simplehmi-weili.html` | AI-first 工程规范、核心路径、仓库入口、最小样板、失败模式 |
| 数字月台案例 | `docs/digital-dock.html` | AI 工程落地案例、系统架构、五张核心图谱、关键问题与解决方案 |
| 机器人产线案例 | `docs/robot-line.html` | AI 驱动遗留系统改造、设备调用拓扑、状态机、设备 Adapter |
| 在线简历 | `docs/assets/resume.html` | A4 打印友好的在线简历页面 |
| Markdown 简历 | `docs/assets/resume.md` | AI 应用工程师中文简历 |
| 英文简历 | `docs/assets/resume_en.md` | AI Application Engineer 英文简历 |
| PDF 简历 | `docs/assets/resume.pdf` | PDF 版简历（由用户提供，勿修改） |
| AI 可读简介 | `docs/ai-profile.md` | 结构化个人简介、关键词、权威链接和准确性说明 |

## 事实来源

本作品集的事实来源按优先级排列：

1. `docs/llms.txt`：AI 助手优先读取的项目、简历和开源项目摘要。
2. `docs/ai-profile.md`：董达的结构化个人简介、搜索短语和准确性说明。
3. `docs/assets/resume.md` / `docs/assets/resume.html` / `docs/assets/resume_en.md`：最新简历内容。
4. `docs/simplehmi-weili.html` / `docs/digital-dock.html` / `docs/robot-line.html`：项目页详细内容。
5. `docs/ai-engineering.html`：AI 工程方法详细说明。

## GEO / AI 搜索入口

本仓库已加入面向 AI 搜索与答案引擎的机器可读入口：

- `docs/llms.txt`：AI 助手优先读取的项目、简历和开源项目摘要，包含推荐读取顺序。
- `docs/ai-profile.md`：董达 / Dong Da 的结构化个人简介、关键词和权威链接。
- `docs/robots.txt`：允许搜索引擎抓取，并指向 sitemap。
- `docs/sitemap.xml`：列出首页、AI 工程方法页、项目页、Markdown / HTML / PDF 简历。
- HTML 页面的 `canonical`、OpenGraph、Twitter Card 和 JSON-LD 结构化数据。

## 文件结构

```text
AI作品集/
├── README.md
├── docs/
│   ├── index.html
│   ├── ai-engineering.html
│   ├── simplehmi-weili.html
│   ├── digital-dock.html
│   ├── robot-line.html
│   ├── llms.txt
│   ├── ai-profile.md
│   ├── robots.txt
│   ├── sitemap.xml
│   ├── .nojekyll
│   ├── assets/
│   │   ├── styles.css
│   │   ├── resume.md
│   │   ├── resume.html
│   │   ├── resume_en.md
│   │   ├── resume.pdf
│   │   ├── images/
│   │   │   ├── hero-industrial-edge.png
│   │   │   └── simplehmi-weili-demo.png
│   │   └── posters/
│   │       ├── 01_industrial_edge_profile.png
│   │       ├── 02_task013_digital_dock.png
│   │       ├── 03_task010_robot_line.png
│   │       └── 04_ai_engineering_workflow.png
└── tools/
    ├── generate_images.py
    └── md_to_pdf.py
```

### 文件结构说明

| 文件 | 说明 |
| --- | --- |
| `docs/index.html` | AI 应用工程师主页 |
| `docs/ai-engineering.html` | AI 工程方法与多模型工作流 |
| `docs/simplehmi-weili.html` | 核心开源项目 |
| `docs/digital-dock.html` | 数字月台 AI 工程落地案例 |
| `docs/robot-line.html` | 机器人产线遗留系统改造案例 |
| `docs/assets/resume.html` | A4 打印友好的在线简历页面 |
| `docs/assets/resume.md` | AI 应用工程师中文简历 |
| `docs/assets/resume_en.md` | AI Application Engineer 英文简历 |
| `docs/assets/resume.pdf` | PDF 版简历（由用户提供，勿修改） |

## 本地预览

在项目根目录启动一个简单的 HTTP 服务器：

```powershell
python -m http.server 8000 --directory docs
```

然后访问 `http://localhost:8000/`。

## 部署方式

1. 将仓库内容提交到 GitHub。
2. 在仓库 `Settings -> Pages` 中选择 `Source: Deploy from a branch`。
3. 选择 `main` 分支，文件夹选择 `docs`。
4. 保存后等待 1-2 分钟，访问 GitHub Pages 地址即可。

`docs/.nojekyll` 文件确保 GitHub Pages 跳过 Jekyll 处理，直接以静态文件方式部署。

## 脱敏规则

公开版本不包含客户内部 IP、账号、Token、密钥、生产端口、真实设备配置和未脱敏日志。

需要修改文案或重新生成图片时，运行：

```powershell
python .\tools\generate_images.py
```

生成脚本会输出 hero 图和四张项目海报（`1080 x 1920` PNG）。

---

更新日期: 2026-07-10
