# 董达｜作品集｜升维看 · 多维做

[中文作品集](https://lx00018310.github.io/) ｜ [English Portfolio](https://lx00018310.github.io/index-en.html)

**Think Higher · Build Wider** ｜ **AI · Strategy · Engineering · Code**

我是董达，擅长破“当局者迷”。我看问题，会拔高一维，直取本质；我做东西，横跨 AI、策划、工程、编程去把它落地。

本项目以 [中文首页](docs/index.html) 和 [英文首页](docs/index-en.html) 为内容定稿依据。简历、AI 资料与分享图使用对应语言的定位和项目表述。

## 三个代表项目

### 考亭古街

**别人困在细节里，我换个方向签下 212 万**

这是文旅项目，我做售前策划方案。当时大家卡在细节和扯皮里出不来，我换了个思路，把项目重新定位成“当地文旅的源头”来讲。客户认可这个方向，最后签下 212 万的合同。

[查看项目](https://lx00018310.github.io/#tourism)

### 数字月台

**不写 PPT，直接进场联调，真机上线**

这是工业现场项目，没有现成模板。我一个人到车间里，把 PLC 和移动机器人直接接起来。设备一多、一断线就容易乱，我用一套统一的状态逻辑把它们的动作管起来。最后是真机联调，上线通过验收。

[查看项目](https://lx00018310.github.io/#industrial)

### EmergentInc

**让 AI 不再只是聊天，而是自动赚钱**

我不满足于 AI 只会聊天。这个开源项目里，AI 能自己跑任务，自己改自己，自动去赚钱。代码全部开源，拿来就能跑。

[查看项目](https://lx00018310.github.io/#emergentinc)

## 本地预览与内容生成

在项目根目录执行以下 Windows 命令：

```powershell
python -m http.server 8080 --directory docs
```

打开 [中文预览](http://localhost:8080/) 或 [英文预览](http://localhost:8080/index-en.html)。

生成脚本与检查：

```powershell
# 生成首页使用的中英文数字月台拓扑图
python -X utf8 tools/generate_visuals.py

# 从分享图模板生成 1200×630 分享图
python -X utf8 tools/og.py

# 从在线简历重新导出 PDF
python -X utf8 tools/html_to_pdf.py

# 更新网站地图
python -X utf8 tools/sitemap.py

# 检查内容、链接、资源、PDF 和浏览器表现
python -X utf8 tools/verify.py
```

运行生成与检查脚本需要 `playwright`、`Pillow`、`pypdf` 和 `beautifulsoup4`，并安装 Playwright Chromium。`tools/generate_images.py` 使用同一分享图生成入口。

## 联系方式与简历

- 姓名：董达 / Dong Da
- 中文定位：AI 顾问
- English role: AI Consultant & Solutions Architect
- 常驻地点：杭州 · 湖州 · 苏州（吴江）
- 电话 / 微信：`18761576008`
- 中文邮箱：`dzpdd@163.com`
- English email: `lx00018310@gmail.com`
- [GitHub 源码](https://github.com/lx00018310)
- [在线简历](https://lx00018310.github.io/assets/resume.html) ｜ [简历 PDF](https://lx00018310.github.io/assets/resume.pdf)
