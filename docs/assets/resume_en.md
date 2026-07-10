# Dong Da - AI Application Engineer

**AI Application Engineer | AI-Driven Software Engineering & Complex System Delivery | Agent Workflows & Engineering Standards**

Phone / WeChat: +86 18761576008
Email: 624290365@qq.com
Portfolio: https://lx00018310.github.io/
GitHub: https://github.com/lx00018310

## Target Roles

AI Application Engineer / AI Engineering Implementation Engineer / AI Coding Engineer / AI Agent Engineer / AI Workflow Engineer / AI Solutions Engineer

## Summary

I use AI Coding Agents to rapidly enter unfamiliar business domains, translating requirements, domain knowledge, and engineering constraints into running systems, then abstract one-off deliveries into reusable Agent workflows, engineering standards, and Engines. With a mechanical engineering and complex project background spanning 16 years, I now focus on AI-driven software engineering, complex system implementation, and production delivery.

My core strength is not writing individual pages or connecting individual devices, but using AI to converge business processes, device signals, legacy systems, frontend and backend systems, terminal interactions, deployment scripts, and exception recovery into a running, reviewable, deliverable, and reusable system.

## Core Competencies

- **AI-driven domain entry and abstraction**: Use AI Coding Agents to read business documents, API specs, legacy source code, device protocols, and field constraints, then produce glossaries, domain objects, call topologies, interface inventories, state machines, risk matrices, and implementation plans before coding.
- **AI Coding and complex system implementation**: Let AI Agents handle search, understanding, generation, review, and documentation within defined boundaries, while humans own goals, boundaries, architecture, risk, and final acceptance, connecting frontend, backend, device integration, data persistence, and deployment.
- **Agent workflow design and Context Engineering**: Establish context, reading order, stage states, deliverables, and gates for AI Agents, orchestrating multi-model planning, implementation, review, fix, and acceptance into a trackable workflow.
- **API, device, and legacy system integration**: Integrate PLCs, robots, face recognition terminals, card readers, inkjet printers, and Java / Vue legacy systems, handling protocol differences, unstable interfaces, concurrency conflicts, and debug boundaries.
- **Production engineering delivery**: State machines, testing, deployment, and exception recovery on Windows industrial PCs with Nginx, NSSM, PowerShell, offline release, integrity verification, version activation, rollback, health checks, and file repair.
- **Abstracting project experience into reusable engineering assets**: Convert one-off deliveries into standards, templates, Skills, Adapters, checklists, and multi-model review workflows so subsequent developers and AI Agents can take over.

## Core Technologies

- **AI Engineering**: AI Coding Agent, Prompt / Context Engineering, multi-model planning, review and repair, Agent Workflow, RAG prototypes, API orchestration, structured output
- **Software Engineering**: Python, TypeScript, JavaScript, Java, React, Vue, Node.js, Fastify, Spring Boot, FastAPI, SQL
- **Systems & Integration**: WebSocket, PostgreSQL, MySQL, SQLite, Redis, state machines, task queues, Adapters, process isolation, Windows deployment
- **Real Device Scenarios**: PLC, robots, face recognition terminals, card readers, inkjet printers, Android Kiosk, industrial HMI

## Featured Projects

### 1. SimpleHmi_WEILI: AI-First Engineering Specification

**Maintainer / Engineering Abstraction | 2026.04 - Present**

Repository: https://github.com/lx00018310/SimpleHmi_WEILI
Project page: https://lx00018310.github.io/simplehmi-weili.html

An AI-first engineering specification extracted from two real complex projects (digital dock and robot line). It targets people who cannot code but can describe field requirements, constraining how an AI reads context, selects a tech stack, plans a system, integrates devices, runs tests, deploys, and submits acceptance evidence, to generate a runnable, deployable, and acceptance-ready industrial system.

**Core work:**
- Designed the AI Agent context entry and reading order (START_HERE -> AGENTS -> SIMPLE_HMI -> ENGINES -> WEILI_LADDER -> docs/00_INDEX).
- Codified "real field first, main chain first, no Mock by default, completion requires evidence" as checkable, interceptable rules.
- Constrained the default lightweight tech stack: React, TypeScript, Vite, Node.js, Fastify.
- Provided templates for requirements, architecture, interface contracts, device integration, configuration, and acceptance.
- Provided a minimal runnable sample (examples/minimal-hmi-system).
- Surfaced common failure modes (coding before understanding requirements, Mock faking real data, only verifying the frontend, ignoring deployment, fixing one issue while breaking another) as checkable, interceptable rules.

**How AI participates:**
The AI Agent is the execution target of this specification. It reads context per the spec, plans before coding, generates frontend, backend, and device Adapters, and on error follows the self-repair spec to search, locate, modify, and re-test, ultimately producing acceptance evidence.

**Reusable output:**
AI-first engineering specification, AI Agent context and reading order, tech stack boundary constraints, No Mock production gate, acceptance checklists, self-repair workflow, minimal runnable sample.

**Status:**
Specification main body, templates, checklists, and minimal runnable sample completed; publicly released and iterating.

---

### 2. Digital Dock: AI Engineering Delivery Case

**Core Developer / System Integration | 2026.03 - Present**

Project page: https://lx00018310.github.io/digital-dock.html

An industrial edge control system for factory auto-loading and digital dock scenarios, comprising a shared industrial PC, 12 touchscreen HMIs, PLCs, a dispatch system, face recognition terminals, and a LAN release system.

**Tech stack:**
React + TypeScript + Vite / Node.js + Fastify + WebSocket / PostgreSQL / SLMP 3E PLC / Python + Hikvision ISUP 5.0 / HMI Agent / Windows industrial PC / Nginx / NSSM / PowerShell

**Core work:**
- HMI frontend with role layering (operator, supervisor, maintenance) and A/B model handling across 12 terminals.
- Node.js / Fastify / WebSocket backend: dock state persistence, task state transitions, event bus, real-time push, crash recovery.
- PLC gateway with exclusive queuing lock to prevent concurrent write conflicts.
- Face recognition service in an isolated Python process (Hikvision ISUP 5.0 SDK), preventing SDK crashes from taking down the main process.
- HMI Agent and deployment controller: `.wrelease` immutable release packages, unified activation, full-network rollback on any node failure (< 90s downtime).
- Windows service hardening with NSSM two-level watchdog, crash restart, deadlock self-heal, and exception file repair.

**How AI participates:**
AI rapidly entered the unfamiliar domains of auto-loading workflows, AGV dispatch interfaces, Mitsubishi PLC, and the Hikvision ISUP C++ SDK. It read and summarized documentation, built system boundaries and glossaries, generated interface and device topologies, assisted with state machine design, generated code, ran consistency reviews, and produced test plans, deployment guides, and troubleshooting SOPs.

**Reusable output:**
HMI Agent, `.wrelease` version packages, deployment controller, Adapter pattern, PLC exclusive queue, state machine templates, health checks, release rollback gates, deployment and troubleshooting SOPs. These were further abstracted into the SimpleHmi_WEILI specification.

**Status:**
Main software chain completed; local integration verified; real-link MVP completed (PLC state aggregation, face recognition real link, HMI LAN version control, deployment self-heal); on-site commissioning in progress; pending on-site acceptance.

---

### 3. Robot Production Line: AI-Driven Legacy System Retrofit

**Core Developer / Device Commissioning | 2026.03 - Present**

Project page: https://lx00018310.github.io/robot-line.html

A field orchestration system for automated catering / exhibition-style production lines, connecting a backend, operator screens, PLCs, card readers, inkjet printers, and delivery robots into a closed loop from card swipe to delivery and return.

**Tech stack:**
Java / Spring Boot / Vue / MySQL / Android Kiosk / Android Robot SDK / PLC / TCP inkjet printer / USB card reader / local HTTP service / Windows industrial PC

**Core work:**
- Consolidated card-swipe, flavor selection, production state, stacking, inkjet printing, robot dispatch, and exception reset flows in Spring Boot + Vue + MySQL.
- Designed a business state machine linking each step into a trackable flow.
- Encapsulated PLC, robot, inkjet, and card reader integration layers for protocol differences and unstable interfaces.
- Built an exclusive card-reading service to prevent port / HID contention.
- Developed an Android robot Kiosk and local HTTP control service for route config, table delivery, manual return, charging, task cancel, and reset.
- Diagnosed and resolved robot API blocking and state lag via serial task queues, async navigation polling, state caching, and Kiosk degradation isolation.
- Built a hardware simulation panel and robot debug API for layered verification.
- Converged production config, separated dev / prod, and cleaned debug entry points from the production chain.

**How AI participates:**
AI rapidly read the Java / Spring Boot / Vue legacy repository, generating class, function, API, database, and device call topologies. It ran consistency reviews across documentation, frontend, backend, and real devices, located blocking chains, assisted with state machine and device Adapter decomposition, and generated fix plans with re-test checklists.

**Reusable output:**
Device Adapters, exclusive card-reading service, serial task queue, state cache, hardware simulation panel, debug API, config and startup script standards. These also fed into the SimpleHmi_WEILI abstraction.

**Status:**
Main flow completed; single-machine testing completed (card swipe, flavor selection, inkjet, PLC state, robot routes, Kiosk control, production config convergence); on-site commissioning in progress; pending on-site acceptance.

---

### 4. Enterprise AI Tools and Multi-Model Workflows

**AI-Assisted Development / Internal Tools / Engineering Standards | 2026.03 - Present**

- Used AI Coding tools for requirements decomposition, code generation, interface sorting, commissioning SOPs, test plans, exception troubleshooting, and project documentation.
- Built internal tools including semi-automated OCR pre-labeling, AI-assisted drawing, and a Feishu bot, combining knowledge retrieval, API orchestration, and human review into executable workflows.
- Established frontend and backend templates and development standards, persisting device adapters, debug isolation, runtime config, health checks, deployment scripts, and progress docs as reusable assets.
- Explored RAG / knowledge base capabilities for managing protocol docs, device manuals, PLC point maps, commissioning logs, and project SOPs.
- Practiced a multi-model collaboration workflow: planning, implementation, review, fix, and acceptance handled by distinct stages with clear inputs, outputs, and gates.

**How AI participates:**
AI is the primary executor across the toolchain, handling retrieval, code generation, documentation, and consistency review; humans own workflow orchestration, result verification, and production boundary control.

**Reusable output:**
Multi-model collaboration workflow, risk classification, definition of done, RAG / knowledge base prototypes, shared templates and development standards.

**Status:**
Multiple internal tools and workflow prototypes completed; iterating.

## Work Experience

### Zhejiang Weili Intelligent Equipment Co., Ltd. | AI Application Engineer / Industrial Edge Application Developer | 2026 - Present

- Developed industrial smart terminals, robot coordination, device integration, AI tools, and deployment systems, driving projects from requirements and protocol analysis to runnable software, on-machine commissioning, and on-site acceptance.
- Contributed to a unified industrial frontend and backend tech stack, forming a "shared core + business config / device adapter layer" reuse pattern.
- Led or deeply participated in the digital dock multi-HMI system and the smart catering line and delivery robot system.
- Improved requirements decomposition, development verification, issue localization, and knowledge retention via AI Coding, engineering docs, automation scripts, and structured progress tracking.
- Abstracted project experience into the SimpleHmi_WEILI open-source specification, validating AI-driven complex system engineering.

### Zhejiang Xianqin Technology Co., Ltd. | New Business Lead | 2020 - 2025

- Responsible for new business planning, resource coordination, solution design, and project delivery, taking multiple innovation projects from 0 to 1.
- Long-term work in customer requirement understanding, solution articulation, cross-team coordination, resource integration, and delivery advancement, laying the foundation for requirements decomposition, project coordination, and field communication in later AI engineering projects.
- Explored AI, digital tools, and new business models, developing the ability to reason backward from business goals to product solutions and delivery paths.

### Zhejiang Shifang Tourism Development Co., Ltd. | Project Lead | 2017 - 2020

- Led planning, coordination, client communication, and cross-team collaboration for large-scale cultural tourism projects.
- Accumulated experience in complex project execution, milestone management, resource coordination, and delivery reviews.
- Developed strong structured solution articulation, risk identification, and multi-party coordination skills, transferable to AI engineering project delivery and client communication.

### Manufacturing Enterprise | Mechanical Engineer | 2010 - 2017

- Industrial product structural design, manufacturing processes, field problem solving, and engineering implementation.
- Familiar with mechanical structures, machining and assembly, production sites, and equipment implementation logic, able to understand hardware constraints, spatial constraints, safety boundaries, and field operation habits in complex projects.
- Composite background enabling the transition from the mechanical field to AI-driven software development, device integration, and complex system applications.

## Education

**North China Electric Power University (211) | Mechanical Design, Manufacturing and Automation | Bachelor | 2006 - 2010**

## Keywords

AI Application Engineer | AI Coding | Agent Workflow | Context Engineering | AI Engineering Implementation | Complex System Development | System Integration | Production Delivery | State Machine | SimpleHmi_WEILI | Industrial Edge (secondary)
