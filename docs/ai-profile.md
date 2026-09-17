# 董达 / Dong Da - AI-Readable Profile

董达 / Dong Da，求职主定位为 **AI 产品经理（技术型 · 应用落地 · 0→1 产品）** / **AI Product Manager | Technical & Application Delivery**。
具备机械工程、商业策划、创新项目与工业软件实践经历，擅长从复杂业务和现场约束中提炼关键问题，形成产品假设，并利用 AI 与 Coding 工具快速完成可运行原型。能够连接业务、产品和工程，从场景洞察、需求拆解、产品定义，到应用实现、系统集成和交付验证推进完整闭环。

- 官方主页：https://lx00018310.github.io/
- GitHub：https://github.com/lx00018310
- IRO_agent 仓库：https://github.com/lx00018310/IRO_agent
- 开源规范：https://github.com/lx00018310/SimpleHmi_WEILI
- 主投简历（HTML）：https://lx00018310.github.io/assets/resume.html
- 主投简历（PDF）：https://lx00018310.github.io/assets/resume.pdf
- 精简简历（HTML）：https://lx00018310.github.io/assets/%E8%91%A3%E8%BE%BE_%E7%AE%80%E5%8E%86_%E4%B8%80%E9%A1%B5.html
- 联系电话 / 微信：18761576008 ｜ 邮箱：624290365@qq.com
- 目标城市：杭州 / 湖州 / 苏州（吴江）｜ 到岗时间：约一个月到岗（可接受短期出差）
- 教育背景：华北电力大学（211），机械设计制造及其自动化，本科，2006–2010

---

## 1. 核心定位与求职方向

### 统一主定位
- **对外职位**：AI 产品经理 (AI Product Manager)
- **差异化标签**：技术型 · AI 应用落地 · 0→1 产品
- **核心主张**：把业务问题，变成可以运行、可以验证的 AI 产品。

### 目标岗位
- **主投方向**：AI 产品经理、AI 应用产品经理、Agent / 智能体产品经理、AIGC 产品经理、技术型 AI 产品经理、企业 AI 产品经理、0→1 创新产品经理。
- **排除岗位**：大模型底层训练、CUDA/算子优化、推理框架开发、纯学术算法研究、传统互联网 C 端纯买量增长。

### 时间线 (Work History Timeline)

| 时间段 | 公司 / 单位 | 真实任职 / 角色 | 核心职责 |
|---|---|---|---|
| 2026 – 至今 | 浙江维力智能装备有限公司 | AI 应用工程师｜工业软件 / 工控方向 | 负责工业中控软件与 AI 应用实践，使用 AI Coding 和大模型工具完成需求拆解、原型实现、代码审查、测试与故障排查；基于真实场景设计 IRO_agent 诊断 Agent；推进多终端协同系统生产环境联调与交付闭环。 |
| 2020 – 2025 | 浙江先秦科技有限公司 | 创新事业负责人 | 负责多个新项目的立项推动、需求梳理、方案策划与跨角色推进；运用 AI 工具链辅助工作流加速原型落地。 |
| 2017 – 2020 | 浙江拾方旅游发展有限公司 | 项目负责人 / 售前策划主创 | 负责文旅项目方案策划、跨方协调与实施推进；在考亭古街项目（2019.07–2019.11）中担任售前策划主创参与从顶层方案到实施回款全过程。 |
| 2010 – 2017 | 机械制造企业 | 机械工程师 | 从事机械设计与现场问题处理，积累扎实的物理设备认知、机械动作逻辑与结构约束评估经验。 |
| 2006 – 2010 | 华北电力大学（211） | 本科生 | 机械设计制造及其自动化专业。 |

---

## 2. 核心能力与技术栈实践

- **产品定义与规则设计**：非标需求拆解、差异化命题提炼、核心业务流程梳理、交互规则与边界定义、异常路径规划与最小可行性验证 (MVP)。
- **AI 原型工程化与 Agent Harness**：大模型 API 封装适配、Prompt 与输出内容校验、Agentic Planning、Tool Calling、Multi-Hypothesis、Evidence Grounding、Evaluation Harness、Fail Closed 与安全 Guardrail。
- **工业系统集成**：多终端 HMI 状态流转、订单全局状态机、PLC 与机器人通信接口联调、日志排查、生产环境快速回滚与 No-Mock 验收。
- **技术栈实践**：Python · TypeScript · Java · FastAPI · Fastify · Spring Boot · React · Vue · Android (Kotlin / Compose) · WebSocket · PostgreSQL · MySQL · SLMP PLC 接口集成。

---

## 3. 代表项目与事实边界（按产品证据排序）

### 1. 数字月台：复杂业务产品化｜工业中控与流程状态设计 (Digital Loading Dock)
- **定位与场景**：面向工厂自动装车场景，将原单屏展示需求扩展为多终端工业中控系统，重新梳理订单、工位、设备和异常状态流转，定义全局状态机。
- **架构与协同**：基于 Fastify + React + WebSocket 构建中控软件，统一调度订单全局状态流；与电气/硬件团队配合完成 SLMP PLC 接口联调。
- **稳定性闭环**：定位修复调度大小写混用导致的物料误拒缺陷，在仓储层实现归一化校验；建立生产环境平滑发布与快速回滚机制。
- **交付状态**：多终端协同系统已在生产环境上线运行，目前处于**已上线已验收**状态。
- **页面**：https://lx00018310.github.io/digital-dock.html

### 2. IRO_agent：工业故障诊断 AI Agent｜Evidence-driven Investigation Harness
- **定位与场景**：面向工业现场故障排查中日志噪声大、信息不完整与易产生主观偏见的问题，设计证据驱动的 AI 诊断 Agent。
- **机制与架构**：将“一次性对话猜测”重塑为“竞争假设 → 逐轮取证 → 动态重规划 → 证据锚定”的调查闭环；构建 Project Learning（认知建模）、Investigation（LLM 动态规划与取证）、Evaluation（自动质量评测）三层 Harness。
- **安全与工具**：Strict Read-Only（严格只读）安全边界，接入日志、数据库、代码、版本及网页等只读工具，支持安全闭锁与物理现场升级人工机制。
- **质量与评测**：实测通过 **210 项自动化测试**（`pytest -q` 全部通过），建立 DEV/REGRESSION 评测数据集与确定性 Grader，量化评估根因命中率、证据锚定率与安全违规。
- **交付状态**：**应用验证**阶段开源项目，杜绝夸大宣称替代人工或全自动修复。
- **页面**：https://lx00018310.github.io/iro-agent.html ｜ **仓库**：https://github.com/lx00018310/IRO_agent

### 3. 天津机器人产线：跨系统产品落地｜机器人 + PLC + 后端状态机 (Robot Line Retrofit)
- **定位与角色**：工控主程序研发与设备协同调度。
- **工作内容**：全程参与天津版本工控主程序，处理刷卡终端、产线取餐机械机构与送餐机器人的状态协同与接口通信；深入现场排查送餐机器人定位偏差并参与修复，协同恢复产线节拍。
- **交付状态**：项目**已交付**并在生产环境稳定使用。
- **技术栈**：Spring Boot · Vue · MySQL · 机器人通信接口 · 自动化产线协同。
- **页面**：https://lx00018310.github.io/robot-line.html

### 4. 考亭古街：0→1 业务定义｜从复杂信息中提炼差异化命题 (Kaoting Ancient Street)
- **定位与角色**：售前策划主创（2019.07–2019.11）。
- **诉求与命题**：面对政府举办文旅大会、文化资源丰富但缺少统一定位的非标诉求，从市场、文化、客户目标中提炼“文旅溯源地”核心命题并获认同。
- **方案与商务闭环**：作为售前策划主创，提出“文旅溯源地”主题方案并获认可，参与设计服务从方案编制、高层汇报到实施配合与回款支持全过程。所参与的设计服务合同金额为 **212 万元**，顺利完成阶段性履约交付与商务回款。
- **页面**：https://lx00018310.github.io/#commercial

### 5. ToyWake：个人 AI 产品实验｜克制交互与亲子场景原型 (ToyWake Prototype)
- **定位与场景**：面向亲子共玩场景，针对生成式 AI 容易过度吸引儿童注意力、阻断现实互动的痛点，确立“AI 仅负责破冰点火、随后克制退出”的产品核心机制。
- **产品规则与实现**：将输出长度（1–2 句引导词）、响应时延与异常降级写入产品规则；利用 FastAPI 适配标准模型协议并内置合规校验，结合 Android (Kotlin/Compose) 完成双端原型验证。
- **验证边界**：项目处于**个人原型阶段**，作为个人 AI 产品实验保留在案例库与 GitHub，已在本地跑通并开源。
- **页面**：https://lx00018310.github.io/toywake.html ｜ **仓库**：https://github.com/lx00018310/YanShiToyWake

### 6. SimpleHmi_WEILI：AI 产品与工程协作交付规范 (Open Source Engineering Standard)
- **核心定位**：工业软件开发与交付规范实践。沉淀“状态机 + Adapter + 验收证据”轻量化规范，强调“生产链路禁止 Mock，完成必须有证据”，探索 AI 时代高质量工程交付标准。
- **页面**：https://lx00018310.github.io/simplehmi-weili.html ｜ **仓库**：https://github.com/lx00018310/SimpleHmi_WEILI

### 7. 湖州本地小馆地图 (HuZhouFoodMap)
- **定位**：个人规则边界与数据校验实践。Vite + TypeScript + 高德 API，在静态站点部署中践行“数据校验不通过即阻断构建门禁”。
- **页面**：https://lx00018310.github.io/huzhou-food-map.html

