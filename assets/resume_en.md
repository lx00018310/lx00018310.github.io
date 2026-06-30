# Dong Da

**Industrial Edge Application Engineer | Industrial IoT & HMI Multi-Terminal Collaboration | PLC, Robotics & Field Device Integration**

Phone / WeChat: +86 18761576008

## Target Position

Industrial Edge Application Engineer / Industrial IoT Application Developer / Smart Manufacturing Software Engineer / Industrial PC Upper Computer Software Engineer / HMI & Field Device Integration Engineer / Intelligent Device System Integration Engineer

## Professional Summary

A versatile professional with a compound background in mechanical design, industrial project management, industrial field software development, and AI-assisted engineering delivery, accumulating 16 years of industrial and project experience. Recently focusing on industrial edge applications, multi-terminal HMI collaboration, PLC and robot device integration, Windows IPC (Industrial PC) deployment, self-healing maintenance, and onsite commissioning.

Proficient across the entire workflow, from requirements analysis, protocol sorting, system architecture, front-end & back-end development, device integration, state machine design, to physical commissioning and deployment. Current focus projects cover public industrial PCs, 12 HMI touch terminals, PLCs, dispatch systems, face recognition devices, robots, RFID card readers, inkjet printers, databases, and local network publishing systems.

Excels at integrating IPCs, HMIs, PLCs, robots, face recognition devices, deployment scripts, and anomaly recovery mechanisms into an onsite debuggable, deployable, and deliverable industrial edge system. Core strength lies in coordinating business processes, device signals, front-end & back-end systems, terminal interactions, deployment scripts, and self-healing mechanisms into a unified, running, and deliverable system under complex industrial field conditions, rather than just isolated page development or hardware connection.

## Core Competencies

* **Industrial Edge Central Control**: Utilizing the public IPC as the central control node to connect HMIs, PLCs, dispatch systems, face recognition devices, and robots, implementing state aggregation, command dispatching, terminal display, log recording, and anomaly recovery.
* **Multi-Terminal HMI Collaboration**: Designing role-based access, permission-based UI display, status synchronization, and simplified interaction for various terminals including 12 touch screens, Android Kiosks, operator screens, line confirmation screens, and venue dashboards.
* **Field Device Integration**: Integrating SLMP 3E PLC, Hikvision ISUP 5.0, face recognition terminals, Android robot SDKs, RFID card readers, inkjet printers, and barcode scanners, with strong capabilities in handling protocol variations, unstable interfaces, field network issues, and debugging boundaries.
* **Deployment & Self-Healing**: Proficient in Windows IPC native service-based deployment, Nginx, NSSM, PowerShell, offline publishing, integrity check, version activation, rollback, health check, and corrupted file auto-recovery.
* **AI-Assisted Development**: Highly experienced in using AI coding and AI workflows for requirements breakdown, document generation, code review, API specification, test planning, and engineering reuse, while prioritizing actual device status, production boundaries, and deliverable results.

## Technical Skills

* **Industrial Edge & Terminals**: Industrial HMI, Android Kiosk, Device Agent, Terminal Heartbeat, Runtime Configuration, Offline Publishing, Remote Upgrade, Fault Recovery, Edge Central Control.
* **Industrial Communication & Protocols**: SLMP 3E PLC, TCP/IP, HTTP, WebSocket, Hikvision ISUP 5.0, Android Robot SDK, RFID Card Reader, Inkjet Printer, Barcode Scanner, Face Recognition Terminal.
* **Back-end & Databases**: TypeScript, Node.js, Fastify, Java, Spring Boot, Python, FastAPI, PostgreSQL, MySQL, SQLite.
* **Front-end & UI/UX**: React, TypeScript, Vite, Vue, Industrial Touchscreen HMI, Operator Panel, Kiosk Full-screen Interaction, Low Cognitive Load UI for Frontline Workers.
* **Deployment & Operations**: Windows IPC, Nginx, PowerShell, NSSM, Docker, Offline Deployment, Batch Upgrade, Version Rollback, Health Check, Log Troubleshooting.
* **AI Engineering**: AI Coding, RAG, API Orchestration, OCR Semi-automatic Labeling, Face Recognition Integration, Engineering Document Automation, Commissioning SOP, Reusable Template Synthesis.

## Key Projects

### Digital Platform Industrial Edge Central Control & Multi-HMI Collaborative System
**Core Developer / System Integrator | Mar 2026 - Present**

**Project Background:**
For factory automated loading and digital platform scenarios, built an industrial edge central control system comprising a public IPC, 12 touchscreen HMIs, PLCs, dispatch systems, face recognition terminals, and a local network publishing system. The system supports platform operation display, personnel verification, device control, alarm handling, status push, unified version publishing, and onsite deployment/recovery.

**Tech Stack:**
React + TypeScript + Vite / Node.js + Fastify + WebSocket / PostgreSQL / SLMP 3E PLC / Python + Hikvision ISUP 5.0 / HMI Agent / Windows IPC / Nginx / NSSM / PowerShell

**Key Responsibilities & Contributions:**
Assumed core development and system integration responsibilities across six key directions:
* **HMI Front-end & Role-based Layers**: Developed vertical full-screen HMI applications using React, TypeScript, and Vite, deploying 12 touchscreen terminals. Built core pages for login verification, job information, device control, alarms, and management debugging. Designed role-based interfaces and permissions (operators, supervisors, maintenance) and handled A/B hardware model variations to minimize frontline operational complexity.
* **Node.js / Fastify / WebSocket Central Back-end**: Developed the central control back-end using Node.js, Fastify, WebSocket, and PostgreSQL. Handled platform state persistence, task state machine flow, event bus, real-time push, critical runtime persistence, and reboot recovery. Built a dispatch system Adapter supporting mock/real modes, centralizing dispatch check-in APIs, DTO validation, structured logging, and exception path handling.
* **PLC Registers & Gateway Integration**: Connected to a physical SLMP 3E PLC gateway, configuring IPs and register addresses for 12 platforms, outlet PLCs, workstations, scanners, face recognition devices, and IPCs. Designed a PLC exclusive queue lock mechanism with background polling, source tagging, and safety interlocking to prevent concurrent write conflicts. Developed HMI client IP binding and validation to restrict unauthorized terminal operations.
* **Face Recognition ISUP Service Commissioning**: Developed an independent face edge service based on Python and Hikvision ISUP 5.0 SDK (process-isolated to prevent SDK crashes from affecting the main system). Integrated device registration, state listening, alarm event parsing, personnel/face image deployment, photo extraction, and workstation binding. Optimized the event path from face recognition to the HMI front-end, resolving issues related to event parsing, SN mapping, image channel blocking, WebSocket push, and front-end UI unresponsiveness.
* **HMI Agent / Deployment Control / Version Rollback**: Designed a deployment controller and HMI daemon agent (PowerShell) to manage terminal authentication, heartbeat monitoring, version management, integrity verification, unified activation, rollback, and offline recovery. Created a `.wrelease` immutable deployment package and version auto-convergence mechanism, supporting LAN-wide publishing, version validation, front-end Mock UI disable verification, and abnormal package interception, ensuring LAN-wide rollback in <90 seconds if any node fails.
* **Windows Service-based Deployment, Self-Healing, and Documentation**: Promoted Windows native green service deployment. Used PowerShell, NSSM, and health check scripts for one-click installation, two-level daemon protection (NSSM auto-restart in 5s + controller active inspection), crash recovery, deadlock self-healing, and corrupted file auto-recovery. Built HMI Bootstrap fallback mechanisms. Maintained strict dev/prod isolation, blocking startups/releases if key configs are missing. Created comprehensive onsite commissioning documents, SOPs, and troubleshooting manuals.

**Project Results:**
* Completed core software pipelines, local integration validation, PLC business state aggregation, face recognition MVP, HMI LAN version control, and deployment self-healing.
* Developed documentation assets including digital platform overall architecture, interface protocols, data models, state machines, PLC registers, onsite deployment, and commissioning acceptance standards.
* Currently executing onsite commissioning and overall acceptance with the public IPC, 12 physical HMIs, PLCs, dispatch, and face recognition devices.

**Transferable Value:**
The capabilities developed here can be applied to smart factories, digital platforms, AGV dispatching, warehousing & logistics, industrial HMIs, industrial edge gateways, unattended terminals, onsite multi-terminal collaboration, and local network publishing systems.

---

### Smart Catering Line & Meal Delivery Robot Collaborative Control System
**Core Developer / Device Commissioning | Mar 2026 - Present**

**Project Background:**
For automated catering/exhibition-style production lines, developed an onsite process orchestration system consisting of an IPC back-end, operator control screen, meal selection/pickup terminals, line confirmation panels, venue dashboards, PLCs, card readers, inkjet printers, and meal delivery robots. The system completes the full loop from card swiping, flavor selection, cup dropping, inkjet printing, and production line transfer to robot food picking, delivery, return, and recharging.

**Tech Stack:**
Java / Spring Boot / Vue / MySQL / Android Kiosk / Android Robot SDK / PLC / TCP Inkjet Printer / USB Card Reader / Local HTTP Service / Windows IPC

**Key Responsibilities & Contributions:**
* Developed operator panels and device monitoring interfaces using Spring Boot, Vue, and MySQL to coordinate card swiping, production state, stacking, printing, robot dispatch, and emergency resets.
* Designed a business state machine connecting card swiping, flavor selection, cup dropping, PLC signal validation, inkjet printing, robot picking, delivery, and return into a fully traceable process.
* Encapsulated integration layers for PLCs, robots, printers, and card readers to handle diverse protocols and unstable onsite interfaces.
* Built a local exclusive card reader service to prevent multiple pages/processes from competing for serial/HID ports, resolving unstable swiping attribution.
* Developed the Android Robot Kiosk and local HTTP control service to implement route configuration, table delivery, manual return, auto-recharge, task cancellation, and unlock-reset functions.
* Troubleshot and resolved robot API blocking and status lag by introducing serial tasks, asynchronous navigation polling, status caching, and Kiosk fallback isolation.
* Handled robot route merging, map canvas rendering, path point configuration, real IP synchronization, map auto-recovery, operational pre-checks, and navigation exception handling.
* Implemented precision pulse jogging, localization recovery, map loading, emergency stop checks, battery level inspection, obstacle avoidance fuse, real-time pose validation, and environmental pre-checks.
* Built a hardware simulation debugging panel and robot debugging APIs to enable layered verification of PLC registers, robot routes, card swiping, and printing during the commissioning phase.
* Streamlined production configuration, separating dev/prod environments and reading critical settings (PLCs, printers, robot callbacks, DB, Redis) from environment variables or a unified config file.
* Cleaned up debugging entry points in the production environment, utilizing conditional loading and launch-blocking configurations to prevent debug interfaces from polluting the production code.
* Added terminal heartbeats, runtime configurations, front-end commissioning launch scripts, back-end production launch scripts, and one-click scripts to open all IPC front-ends, boosting onsite deployment efficiency.

**Project Results:**
* Completed main process flows and single-machine testing, delivering core capabilities for card swiping, flavor selection, printing, PLC states, robot routes, Kiosk control, and configuration convergence.
* Troubleshot and resolved major bugs including robot API lag, map loading/recovery, shutdown sequence, delivery routes, multi-table route merging, and card reader service conflict.
* Currently advancing onsite acceptance with physical PLCs, complete robot routes, printing templates, and multi-device coordination.

**Transferable Value:**
Capabilities are transferable to automated catering, exhibition automation, service robots, smart stores, robot delivery, industrial process orchestration, device interlocking control, and onsite debugging platforms.

---

### Enterprise AI Tools & Engineering Asset Development
**AI-Assisted Development / Internal Tools / Engineering Standards | Mar 2026 - Present**

* Utilized AI coding tools to assist in requirements breakdown, code generation, API specification, commissioning SOPs, test plans, troubleshooting, and project documentation, significantly improving efficiency in complex industrial projects.
* Developed internal tools including semi-automatic OCR labeling, AI-assisted diagram generation, and corporate Feishu (Lark) bots, combining knowledge retrieval and API orchestration with manual review into executable workflows.
* Built unified industrial front-end and back-end templates and development standards, establishing reusable assets for device adaptation, debug isolation, runtime configurations, health checks, deployment scripts, and project timeline tracking.
* Explored RAG/knowledge base applications for industrial projects to manage protocol documents, device manuals, PLC registers, commissioning logs, anomaly reports, and project SOPs, enabling rapid startup of subsequent projects.

## Professional Experience

### Zhejiang Weili Intelligent Equipment Co., Ltd. | AI Engineer / Industrial Edge App Developer | 2026 - Present
* Responsible for industrial smart terminals, robot collaboration, device integration, AI tools, and deployment systems, driving projects from requirements and protocol clarification to running software, physical commissioning, and onsite acceptance.
* Participated in building the company's unified industrial tech stack, establishing a reusable framework of "common core + business configuration/device adaptation layer".
* Lead or deeply participated in projects like the Digital Platform Multi-HMI Collaborative System and Smart Catering & Delivery Robot Collaborative System, covering front-end, back-end, PLCs, robots, face recognition, deployment scripts, and onsite commissioning.
* Improved efficiency in requirement analysis, dev validation, troubleshooting, and knowledge accumulation through AI coding, engineering docs, automated scripts, and standardized progress logs.

### Zhejiang Xianqin Technology Co., Ltd. | Head of New Business | 2020 - 2025
* Responsible for new business planning, resource coordination, solution design, and project execution, driving multiple innovative projects from 0 to 1.
* Managed client requirement gathering, solution presentation, cross-team coordination, resource integration, and delivery management, laying a solid foundation for requirement breakdown, project management, and onsite communication in software projects.
* Explored AI integration, digital tools, and new business models, developing the capability to reverse-engineer product solutions and implementation paths from business goals.

### Zhejiang Shifang Tourism Development Co., Ltd. | Project Manager | 2017 - 2020
* Responsible for large-scale cultural tourism project planning, overall management, client communication, and cross-team collaboration.
* Managed projects such as the Jianyang Kaoting Cultural Tourism Zone, gaining extensive experience in complex project execution, milestone management, resource coordination, and delivery review.
* Developed strong structural presentation, risk identification, and multi-party coordination skills, which are highly transferable to industrial project management and client communication.

### Mechanical Manufacturing Enterprises | Mechanical Engineer | 2010 - 2017
* Engaged in structural design of industrial products, manufacturing processes, onsite troubleshooting, and engineering implementation.
* Familiar with mechanical structures, machining, assembly, production floors, and equipment deployment logic. Able to understand hardware constraints, spatial limitations, safety boundaries, and onsite operator habits in industrial projects.
* Possesses a compound background transitioning from mechanical engineering to industrial software, device integration, and smart manufacturing applications.

## Education

**North China Electric Power University (211 Project)**  
*Bachelor of Engineering in Mechanical Design, Manufacturing and Automation | 2006 - 2010*

## Keywords

Industrial Edge Applications | HMI Multi-Terminal Collaboration | PLC Integration | Robot Control | Face Recognition Devices | Windows IPC Deployment | Onsite Commissioning | State Machine | WebSocket | Device Heartbeats | Version Release & Rollback | AI-Assisted Development | Industrial Project Delivery
