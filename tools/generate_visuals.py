"""
tools/generate_visuals.py
按《作品集视觉化改造与内容纠偏 Plan》第 4 节素材清单生成 V01–V11 的矢量图形
"""
from pathlib import Path

VISUALS_DIR = Path("docs/assets/visuals")
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

def create_v01():
    # V01: hero-solutions.svg (640x360) 首页首屏三大物件
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="100%" height="100%" role="img" aria-label="方案表达、软件集成与AI原型三大能力视觉物件">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="640" height="360" fill="#FAF5FF" rx="16"/>
  
  <!-- 1. 方案表达卡片 (左) -->
  <g transform="translate(24, 38)" filter="url(#shadow)">
    <rect width="180" height="284" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="180" height="42" rx="14" fill="#ECFEFF"/>
    <rect y="28" width="180" height="14" fill="#ECFEFF"/>
    <circle cx="22" cy="21" r="5" fill="#0891B2"/>
    <text x="36" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#0891B2">方案表达</text>
    
    <rect x="18" y="58" width="90" height="10" rx="3" fill="#0F172A" opacity="0.85"/>
    <rect x="18" y="76" width="144" height="6" rx="3" fill="#C7C7CC"/>
    <rect x="18" y="88" width="130" height="6" rx="3" fill="#C7C7CC"/>
    <rect x="18" y="100" width="138" height="6" rx="3" fill="#C7C7CC"/>

    <rect x="18" y="122" width="144" height="48" rx="8" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="28" y="142" font-family="monospace" font-size="11" font-weight="600" fill="#0F172A">诉求拆解与定位</text>
    <text x="28" y="157" font-family="sans-serif" font-size="10" fill="#475569">文旅溯源地 / 业务闭环</text>

    <rect x="18" y="184" width="144" height="78" rx="8" fill="#ECFEFF" stroke="#CFFAFE"/>
    <text x="28" y="204" font-family="sans-serif" font-size="11" font-weight="700" fill="#0891B2">设计服务合同额</text>
    <text x="28" y="232" font-family="sans-serif" font-size="22" font-weight="800" fill="#0F172A">212 <tspan font-size="13" font-weight="600" fill="#475569">万元</tspan></text>
    <text x="28" y="250" font-family="sans-serif" font-size="10" fill="#64748B">售前策划主创参与全过程</text>
  </g>

  <!-- 2. 软件集成卡片 (中 - 主题蓝色强调) -->
  <g transform="translate(222, 22)" filter="url(#shadow)">
    <rect width="210" height="316" rx="16" fill="#FFFFFF" stroke="#D946EF" stroke-width="2"/>
    <rect width="210" height="46" rx="16" fill="#D946EF"/>
    <rect y="30" width="210" height="16" fill="#D946EF"/>
    <rect x="16" y="17" width="12" height="12" rx="2" fill="#FFFFFF"/>
    <text x="36" y="27" font-family="sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">工控软件集成</text>
    
    <!-- 工业触摸屏 HMI 界面模拟 -->
    <rect x="16" y="60" width="178" height="96" rx="8" fill="#0F172A"/>
    <rect x="24" y="70" width="76" height="8" rx="2" fill="#D946EF"/>
    <rect x="154" y="70" width="30" height="8" rx="3" fill="#34C759"/>
    
    <text x="24" y="100" font-family="monospace" font-size="10" fill="#64748B">工位01 [自动装车联动]</text>
    <rect x="24" y="106" width="110" height="5" rx="2.5" fill="#D946EF"/>
    <text x="24" y="128" font-family="monospace" font-size="10" fill="#64748B">订单状态机 [已上线已验收]</text>
    <rect x="24" y="134" width="144" height="5" rx="2.5" fill="#34C759"/>

    <!-- 中控服务 -->
    <rect x="16" y="168" width="178" height="60" rx="8" fill="#FDF4FF" stroke="#F5D0FE"/>
    <text x="26" y="188" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">Fastify + WebSocket</text>
    <text x="26" y="206" font-family="sans-serif" font-size="10" fill="#475569">全局状态机 ⇄ 多端状态推送</text>

    <!-- 设备与接口 -->
    <rect x="16" y="240" width="178" height="60" rx="8" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="26" y="260" font-family="sans-serif" font-size="11" font-weight="700" fill="#0F172A">多系统协议联调</text>
    <text x="26" y="278" font-family="sans-serif" font-size="10" fill="#475569">PLC 联锁 ｜ 调度对接 ｜ 进程隔离</text>
  </g>

  <!-- 3. AI 原型卡片 (右) -->
  <g transform="translate(450, 38)" filter="url(#shadow)">
    <rect width="166" height="284" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="166" height="42" rx="14" fill="#F8FAFC"/>
    <rect y="28" width="166" height="14" fill="#F8FAFC"/>
    <circle cx="22" cy="21" r="5" fill="#475569"/>
    <text x="34" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#475569">AI 原型构建</text>

    <!-- 手机屏幕外框 -->
    <rect x="20" y="56" width="126" height="142" rx="10" fill="#FAFCFD" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="52" y="62" width="62" height="4" rx="2" fill="#CBD5E1"/>
    
    <rect x="28" y="78" width="76" height="8" rx="2" fill="#475569" opacity="0.2"/>
    <text x="30" y="85" font-family="sans-serif" font-size="8" font-weight="600" fill="#475569">玩具标签: 积木小车</text>
    
    <!-- 提示气泡 -->
    <rect x="28" y="94" width="110" height="44" rx="6" fill="#F1F5F9"/>
    <text x="34" y="110" font-family="sans-serif" font-size="9" font-weight="600" fill="#0F172A">“小车准备出发！”</text>
    <text x="34" y="125" font-family="sans-serif" font-size="8" fill="#475569">（简短启发，设备退出）</text>

    <!-- 兜底状态 -->
    <rect x="28" y="148" width="110" height="22" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="34" y="162" font-family="monospace" font-size="8" fill="#34C759">✓ 本地固定内容兜底</text>

    <rect x="18" y="214" width="130" height="48" rx="8" fill="#FAF5FF"/>
    <text x="26" y="234" font-family="sans-serif" font-size="10" font-weight="700" fill="#0F172A">双端原型跑通</text>
    <text x="26" y="250" font-family="sans-serif" font-size="9" fill="#475569">FastAPI + Android (Compose)</text>
  </g>
</svg>'''
    (VISUALS_DIR / "hero-solutions.svg").write_text(svg, encoding="utf-8")


def create_v02():
    # V02: dock-system.svg (720x400) 数字月台分层架构拓扑图
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 400" width="100%" height="100%" role="img" aria-label="数字月台分层架构拓扑与职责边界">
  <rect width="720" height="400" fill="#FAFCFD" rx="14"/>
  <rect x="12" y="12" width="696" height="376" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>

  <text x="28" y="42" font-family="sans-serif" font-size="16" font-weight="700" fill="#0F172A">数字月台：系统拓扑与职责边界</text>
  <text x="28" y="62" font-family="sans-serif" font-size="12" fill="#475569">中心高亮区域为本人负责工控软件系统，外部灰色节点为专业协作接口</text>

  <!-- 外部上层系统 (左上) -->
  <g transform="translate(36, 92)">
    <rect width="170" height="96" rx="8" fill="#FAF5FF" stroke="#CBD5E1" stroke-dasharray="4,3"/>
    <text x="16" y="28" font-family="sans-serif" font-size="11" font-weight="700" fill="#64748B">外部协同系统</text>
    <text x="16" y="48" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">企业上层调度系统</text>
    <text x="16" y="66" font-family="sans-serif" font-size="11" fill="#475569">订单计划下发 / 状态回执</text>
    <text x="16" y="82" font-family="monospace" font-size="10" fill="#D946EF">HTTP / Webhook</text>
  </g>

  <!-- 外部人脸/刷卡服务 (左下) -->
  <g transform="translate(36, 218)">
    <rect width="170" height="96" rx="8" fill="#FAF5FF" stroke="#CBD5E1" stroke-dasharray="4,3"/>
    <text x="16" y="28" font-family="sans-serif" font-size="11" font-weight="700" fill="#64748B">外部协同系统</text>
    <text x="16" y="48" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">人脸与刷卡桥接服务</text>
    <text x="16" y="66" font-family="sans-serif" font-size="11" fill="#475569">现场司机身份核验</text>
    <text x="16" y="82" font-family="monospace" font-size="10" fill="#D946EF">进程级异常隔离</text>
  </g>

  <!-- 中央高亮区域：本人负责软件体系 -->
  <g transform="translate(236, 84)">
    <!-- 外框 -->
    <rect width="268" height="240" rx="12" fill="#FDF4FF" stroke="#D946EF" stroke-width="2"/>
    <rect width="268" height="32" rx="12" fill="#D946EF"/>
    <rect y="20" width="268" height="12" fill="#D946EF"/>
    <text x="16" y="21" font-family="sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">本人负责：工控软件系统</text>

    <!-- 中控核心服务 -->
    <rect x="16" y="44" width="236" height="88" rx="8" fill="#FFFFFF" stroke="#F5D0FE"/>
    <text x="28" y="68" font-family="sans-serif" font-size="14" font-weight="700" fill="#D946EF">中控业务服务 (Fastify)</text>
    <text x="28" y="86" font-family="sans-serif" font-size="11" fill="#0F172A">全局订单状态机 ｜ PostgreSQL 履历持久化</text>
    <text x="28" y="104" font-family="sans-serif" font-size="11" fill="#475569">物料大小写归一化 ｜ 剩余额度防超入账</text>
    <text x="28" y="120" font-family="monospace" font-size="10" fill="#34C759">状态：已上线已验收</text>

    <!-- 双向箭头 -->
    <path d="M 134 136 L 134 150" stroke="#D946EF" stroke-width="2" stroke-dasharray="3,2"/>
    <polygon points="134,134 131,140 137,140" fill="#D946EF"/>
    <polygon points="134,152 131,146 137,146" fill="#D946EF"/>
    <text x="144" y="146" font-family="monospace" font-size="9" fill="#D946EF">WebSocket 实时推送</text>

    <!-- 前端触摸屏 HMI -->
    <rect x="16" y="154" width="236" height="72" rx="8" fill="#FFFFFF" stroke="#F5D0FE"/>
    <text x="28" y="178" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">多工位 HMI 界面 (React + TS)</text>
    <text x="28" y="196" font-family="sans-serif" font-size="11" fill="#475569">工位订单状态呈现 / 现场人工确认闭环</text>
    <text x="28" y="212" font-family="sans-serif" font-size="10" fill="#64748B">触摸屏多终端分发</text>
  </g>

  <!-- 外部 PLC 联控系统 (右侧) -->
  <g transform="translate(534, 150)">
    <rect width="156" height="110" rx="8" fill="#FAF5FF" stroke="#CBD5E1" stroke-dasharray="4,3"/>
    <text x="14" y="26" font-family="sans-serif" font-size="11" font-weight="700" fill="#64748B">外部专业协作</text>
    <text x="14" y="46" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">现场 PLC 控制系统</text>
    <text x="14" y="64" font-family="sans-serif" font-size="11" fill="#475569">自动装车联锁信号</text>
    <text x="14" y="80" font-family="sans-serif" font-size="11" fill="#64748B">电气硬件由专人负责</text>
    <text x="14" y="98" font-family="monospace" font-size="10" fill="#D946EF">SLMP 协议联调</text>
  </g>

  <!-- 连接线 -->
  <!-- 调度系统 -> 中控 -->
  <path d="M 206 140 L 236 140" stroke="#D946EF" stroke-width="2"/>
  <polygon points="236,140 228,136 228,144" fill="#D946EF"/>

  <!-- 人脸桥 -> 中控 -->
  <path d="M 206 266 L 236 266" stroke="#D946EF" stroke-width="2"/>
  <polygon points="236,266 228,262 228,270" fill="#D946EF"/>

  <!-- 中控 <-> PLC -->
  <path d="M 504 205 L 534 205" stroke="#D946EF" stroke-width="2"/>
  <polygon points="534,205 526,201 526,209" fill="#D946EF"/>
  <polygon points="504,205 512,201 512,209" fill="#D946EF"/>

  <!-- 底部说明 -->
  <rect x="28" y="344" width="664" height="30" rx="6" fill="#FAF5FF"/>
  <text x="360" y="363" font-family="sans-serif" font-size="11" fill="#64748B" text-anchor="middle">系统关系示意，非部署规模 ｜ 本人负责中间蓝色软件研发与协议对接，现场 PLC 控制程序与电气硬件由公司其他专业人员负责</text>
</svg>'''
    (VISUALS_DIR / "dock-system.svg").write_text(svg, encoding="utf-8")


def create_v03():
    # V03: dock-flow.svg (720x240) 数据流与分工色带
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 240" width="100%" height="100%" role="img" aria-label="数字月台业务流转与职责色带">
  <rect width="720" height="240" fill="#FAFCFD" rx="12"/>
  <rect x="10" y="10" width="700" height="220" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>

  <text x="24" y="36" font-family="sans-serif" font-size="15" font-weight="700" fill="#0F172A">订单与装车协同流转逻辑</text>

  <!-- 4 个流转节点 -->
  <!-- 节点 1: 外部调度推送 -->
  <g transform="translate(24, 60)">
    <rect width="144" height="96" rx="8" fill="#FAF5FF" stroke="#CBD5E1"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#64748B">1. 外部输入</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#0F172A">调度订单推送</text>
    <text x="12" y="64" font-family="sans-serif" font-size="11" fill="#475569">装车批次、物料编码</text>
    <text x="12" y="82" font-family="monospace" font-size="10" fill="#D946EF">大小写混用待规范</text>
  </g>

  <!-- 箭头 1->2 -->
  <path d="M 172 108 L 194 108" stroke="#D946EF" stroke-width="2"/>
  <polygon points="194,108 186,104 186,112" fill="#D946EF"/>

  <!-- 节点 2: 中控状态机与校验 (核心高亮) -->
  <g transform="translate(196, 52)">
    <rect width="180" height="112" rx="8" fill="#FDF4FF" stroke="#D946EF" stroke-width="2"/>
    <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">2. 本人负责：软件核心</text>
    <text x="12" y="42" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">中控状态机推进</text>
    <text x="12" y="62" font-family="sans-serif" font-size="11" fill="#475569">编码归一化与额度合并</text>
    <text x="12" y="80" font-family="sans-serif" font-size="11" fill="#475569">防超额入账 / 事务同步</text>
    <text x="12" y="98" font-family="monospace" font-size="10" fill="#34C759">支持异常版本快速回退</text>
  </g>

  <!-- 箭头 2->3 -->
  <path d="M 380 108 L 402 108" stroke="#D946EF" stroke-width="2"/>
  <polygon points="402,108 394,104 394,112" fill="#D946EF"/>

  <!-- 节点 3: 多端 HMI 同步 -->
  <g transform="translate(404, 60)">
    <rect width="144" height="96" rx="8" fill="#FDF4FF" stroke="#D946EF"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">3. 本人负责：界面</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#0F172A">触摸屏 HMI 同步</text>
    <text x="12" y="64" font-family="sans-serif" font-size="11" fill="#475569">WebSocket 实时广播</text>
    <text x="12" y="82" font-family="sans-serif" font-size="10" fill="#475569">工位状态确认 / 异常呈现</text>
  </g>

  <!-- 箭头 3->4 -->
  <path d="M 552 108 L 574 108" stroke="#D946EF" stroke-width="2"/>
  <polygon points="574,108 566,104 566,112" fill="#D946EF"/>

  <!-- 节点 4: PLC 与物理设备 -->
  <g transform="translate(576, 60)">
    <rect width="120" height="96" rx="8" fill="#FAF5FF" stroke="#CBD5E1"/>
    <text x="10" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#64748B">4. 外部专业</text>
    <text x="10" y="44" font-family="sans-serif" font-size="12" font-weight="700" fill="#0F172A">PLC 联锁作业</text>
    <text x="10" y="64" font-family="sans-serif" font-size="11" fill="#475569">装车机构就绪</text>
    <text x="10" y="82" font-family="sans-serif" font-size="10" fill="#64748B">硬件电气专业协作</text>
  </g>

  <!-- 底部色带图例 -->
  <g transform="translate(24, 184)">
    <rect x="0" y="4" width="14" height="14" rx="3" fill="#D946EF"/>
    <text x="22" y="16" font-family="sans-serif" font-size="11.5" font-weight="600" fill="#0F172A">本人负责：软件中控研发、HMI 交互与接口适配</text>
    <rect x="360" y="4" width="14" height="14" rx="3" fill="#64748B"/>
    <text x="382" y="16" font-family="sans-serif" font-size="11.5" font-weight="600" fill="#475569">其他专业：现场 PLC 梯形图、电气接线与机械硬件</text>
  </g>
</svg>'''
    (VISUALS_DIR / "dock-flow.svg").write_text(svg, encoding="utf-8")


def create_v04():
    # V04: robot-process.svg (720x220) 天津产线协同流程图
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 220" width="100%" height="100%" role="img" aria-label="天津机器人产线协同流程示意">
  <rect width="720" height="220" fill="#FAFCFD" rx="12"/>
  <rect x="10" y="10" width="700" height="200" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>

  <text x="24" y="36" font-family="sans-serif" font-size="15" font-weight="700" fill="#0F172A">天津机器人产线：工控主程序与取送餐协同流程</text>

  <!-- 4 步协同流程 -->
  <!-- 步骤 1 -->
  <g transform="translate(24, 56)">
    <rect width="146" height="96" rx="8" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">阶段 1: 身份触发</text>
    <text x="12" y="46" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">终端扫码 / 刷卡</text>
    <text x="12" y="66" font-family="sans-serif" font-size="11" fill="#475569">用户刷卡发起就餐</text>
    <text x="12" y="82" font-family="monospace" font-size="10" fill="#64748B">网络事件传递至主程序</text>
  </g>

  <path d="M 174 104 L 194 104" stroke="#D946EF" stroke-width="2"/>
  <polygon points="194,104 186,100 186,108" fill="#D946EF"/>

  <!-- 步骤 2 (本人主程序) -->
  <g transform="translate(196, 50)">
    <rect width="168" height="108" rx="8" fill="#FDF4FF" stroke="#D946EF" stroke-width="2"/>
    <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">阶段 2: 本人负责</text>
    <text x="12" y="42" font-family="sans-serif" font-size="13.5" font-weight="700" fill="#0F172A">工控主程序调度</text>
    <text x="12" y="62" font-family="sans-serif" font-size="11" fill="#475569">订单状态校验与匹配</text>
    <text x="12" y="80" font-family="sans-serif" font-size="11" fill="#475569">协调取餐就绪检测</text>
    <text x="12" y="98" font-family="monospace" font-size="10" fill="#34C759">调度送餐机器人启程</text>
  </g>

  <path d="M 368 104 L 388 104" stroke="#D946EF" stroke-width="2"/>
  <polygon points="388,104 380,100 380,108" fill="#D946EF"/>

  <!-- 步骤 3 -->
  <g transform="translate(390, 56)">
    <rect width="146" height="96" rx="8" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">阶段 3: 产线对接</text>
    <text x="12" y="46" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">机械臂取餐移载</text>
    <text x="12" y="66" font-family="sans-serif" font-size="11" fill="#475569">就绪到位检测闭环</text>
    <text x="12" y="82" font-family="monospace" font-size="10" fill="#64748B">完成信号反馈主程序</text>
  </g>

  <path d="M 540 104 L 560 104" stroke="#D946EF" stroke-width="2"/>
  <polygon points="560,104 552,100 552,108" fill="#D946EF"/>

  <!-- 步骤 4 -->
  <g transform="translate(562, 56)">
    <rect width="134" height="96" rx="8" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="10" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">阶段 4: 设备投递</text>
    <text x="10" y="46" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">送餐机器人行进</text>
    <text x="10" y="66" font-family="sans-serif" font-size="11" fill="#475569">自主导航至就餐位</text>
    <text x="10" y="82" font-family="monospace" font-size="10" fill="#34C759">状态：已交付</text>
  </g>

  <rect x="24" y="172" width="672" height="26" rx="4" fill="#FAF5FF"/>
  <text x="360" y="189" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="middle">协同流程示意 ｜ 本人参与送餐机器人定位偏差问题的排查修复；项目已交付并在生产环境使用</text>
</svg>'''
    (VISUALS_DIR / "robot-process.svg").write_text(svg, encoding="utf-8")


def create_v05():
    # V05: toywake-story.svg (720x240) ToyWake 三步分镜交互图
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 240" width="100%" height="100%" role="img" aria-label="ToyWake 亲子共玩三步分镜交互示意">
  <rect width="720" height="240" fill="#FAFCFD" rx="12"/>
  <rect x="10" y="10" width="700" height="220" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>

  <text x="24" y="34" font-family="sans-serif" font-size="15" font-weight="700" fill="#0F172A">ToyWake：克制式交互分镜（让设备退到后台）</text>

  <!-- 3 个分镜 -->
  <!-- 分镜 1 -->
  <g transform="translate(24, 52)">
    <rect width="210" height="136" rx="8" fill="#FAFCFD" stroke="#E2E8F0"/>
    <rect width="210" height="28" rx="8" fill="#F1F5F9"/>
    <rect y="20" width="210" height="8" fill="#F1F5F9"/>
    <text x="12" y="19" font-family="sans-serif" font-size="11" font-weight="700" fill="#475569">Step 1: 现实玩具触发</text>
    
    <text x="14" y="52" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">围绕已有积木 / 玩偶</text>
    <text x="14" y="74" font-family="sans-serif" font-size="11" fill="#475569">孩子面前是真实的物理玩具，</text>
    <text x="14" y="92" font-family="sans-serif" font-size="11" fill="#475569">家长在手机选择或轻触玩具标签。</text>
    <rect x="14" y="106" width="100" height="20" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="20" y="120" font-family="monospace" font-size="10" fill="#475569">标签: [小恐龙/积木]</text>
  </g>

  <!-- 分镜 2 -->
  <g transform="translate(254, 52)">
    <rect width="212" height="136" rx="8" fill="#FAFCFD" stroke="#475569" stroke-width="1.5"/>
    <rect width="212" height="28" rx="8" fill="#475569"/>
    <rect y="20" width="212" height="8" fill="#475569"/>
    <text x="12" y="19" font-family="sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">Step 2: 1 句简短引导提示</text>
    
    <!-- 气泡 -->
    <rect x="14" y="42" width="184" height="50" rx="6" fill="#F1F5F9"/>
    <text x="22" y="62" font-family="sans-serif" font-size="12" font-weight="600" fill="#0F172A">“一只小恐龙准备出发了，”</text>
    <text x="22" y="80" font-family="sans-serif" font-size="11" fill="#475569">“它要跨过前面的积木城堡！”</text>

    <text x="14" y="112" font-family="sans-serif" font-size="11" fill="#475569">不展开无休止多轮对话，</text>
    <text x="14" y="128" font-family="sans-serif" font-size="11" fill="#475569">单次播报仅作为剧情开端。</text>
  </g>

  <!-- 分镜 3 -->
  <g transform="translate(486, 52)">
    <rect width="210" height="136" rx="8" fill="#FAFCFD" stroke="#E2E8F0"/>
    <rect width="210" height="28" rx="8" fill="#F1F5F9"/>
    <rect y="20" width="210" height="8" fill="#F1F5F9"/>
    <text x="12" y="19" font-family="sans-serif" font-size="11" font-weight="700" fill="#475569">Step 3: 设备静默与退出</text>
    
    <text x="14" y="52" font-family="sans-serif" font-size="13" font-weight="700" fill="#0F172A">手机进入静默待命</text>
    <text x="14" y="74" font-family="sans-serif" font-size="11" fill="#475569">不追问、不打扰现实游戏，</text>
    <text x="14" y="92" font-family="sans-serif" font-size="11" fill="#475569">设备退至一旁，孩子与家长</text>
    <text x="14" y="110" font-family="sans-serif" font-size="11" fill="#0F172A" font-weight="600">回归现实人际面对面互动。</text>
  </g>

  <rect x="24" y="198" width="672" height="24" rx="4" fill="#FAF5FF"/>
  <text x="360" y="214" font-family="sans-serif" font-size="11" fill="#64748B" text-anchor="middle">交互分镜示意 ｜ 状态：个人原型 ｜ 旨在探索克制化生成式 AI 交互，不设商业 KPI</text>
</svg>'''
    (VISUALS_DIR / "toywake-story.svg").write_text(svg, encoding="utf-8")


def create_v06():
    # V06: toywake-response.svg (720x260) 后端模型适配与双层降级
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 260" width="100%" height="100%" role="img" aria-label="ToyWake 后端适配与平滑降级流程">
  <rect width="720" height="260" fill="#FAFCFD" rx="12"/>
  <rect x="10" y="10" width="700" height="240" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>

  <text x="24" y="34" font-family="sans-serif" font-size="15" font-weight="700" fill="#0F172A">后端模型接口适配与双层降级机制</text>

  <!-- 客户端请求 -->
  <g transform="translate(24, 60)">
    <rect width="130" height="88" rx="8" fill="#FAF5FF" stroke="#CBD5E1"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#0F172A">客户端发起请求</text>
    <text x="12" y="44" font-family="monospace" font-size="10" fill="#475569">POST /v1/prompt</text>
    <text x="12" y="62" font-family="sans-serif" font-size="11" fill="#475569">携带玩具标签</text>
    <text x="12" y="78" font-family="sans-serif" font-size="10" fill="#64748B">FastAPI 接收</text>
  </g>

  <!-- 箭头 -->
  <path d="M 154 104 L 180 104" stroke="#D946EF" stroke-width="2"/>
  <polygon points="180,104 172,100 172,108" fill="#D946EF"/>

  <!-- 模型调用与校验 (实线正常路径) -->
  <g transform="translate(182, 50)">
    <rect width="210" height="108" rx="8" fill="#FDF4FF" stroke="#D946EF" stroke-width="1.5"/>
    <text x="12" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">主路径: 外部模型适配</text>
    <text x="12" y="42" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#0F172A">OpenAI 兼容接口封装</text>
    <text x="12" y="60" font-family="sans-serif" font-size="11" fill="#475569">HTTP 请求 / 超时与异常捕获</text>
    <text x="12" y="78" font-family="sans-serif" font-size="11" fill="#475569">输出字段与长度安全校验</text>
    <text x="12" y="96" font-family="monospace" font-size="10" fill="#34C759">校验成功: source=model</text>
  </g>

  <!-- 箭头 正常输出 -->
  <path d="M 392 104 L 540 104" stroke="#34C759" stroke-width="2"/>
  <polygon points="540,104 532,100 532,108" fill="#34C759"/>
  <text x="446" y="96" font-family="sans-serif" font-size="10" fill="#34C759">格式校验通过</text>

  <!-- 兜底降级库 (虚线降级路径) -->
  <g transform="translate(220, 172)">
    <rect width="280" height="64" rx="8" fill="#ECFEFF" stroke="#CFFAFE" stroke-dasharray="4,3"/>
    <text x="14" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#0891B2">兜底路径: 本地固定提示库 (fixed_contents)</text>
    <text x="14" y="40" font-family="sans-serif" font-size="11" fill="#475569">未配 Key 默认启动 ｜ API 超时 / 异常 / 校验不合格自动切换</text>
    <text x="14" y="56" font-family="monospace" font-size="10" fill="#0891B2">平滑降级: source=fixed (不向前端报错)</text>
  </g>

  <!-- 降级虚线 -->
  <path d="M 287 158 L 287 172" stroke="#0891B2" stroke-width="2" stroke-dasharray="3,3"/>
  <path d="M 500 204 L 540 204 L 540 134" stroke="#0891B2" stroke-width="2" stroke-dasharray="3,3"/>
  <polygon points="540,134 536,142 544,142" fill="#0891B2"/>

  <!-- 输出终端 -->
  <g transform="translate(542, 60)">
    <rect width="150" height="88" rx="8" fill="#FAF5FF" stroke="#CBD5E1"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#0F172A">终端接收引导语</text>
    <text x="12" y="46" font-family="sans-serif" font-size="12" font-weight="600" fill="#D946EF">1-2 句简短引导</text>
    <text x="12" y="66" font-family="sans-serif" font-size="10.5" fill="#475569">带来源标识</text>
    <text x="12" y="80" font-family="monospace" font-size="10" fill="#34C759">体验不中断</text>
  </g>
</svg>'''
    (VISUALS_DIR / "toywake-response.svg").write_text(svg, encoding="utf-8")


def create_v09():
    # V09: ai-workflow.svg (720x260) AI 辅助开发闭环与证据层级
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 260" width="100%" height="100%" role="img" aria-label="AI 辅助开发闭环与证据层级">
  <rect width="720" height="260" fill="#FAFCFD" rx="12"/>
  <rect x="10" y="10" width="700" height="240" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>

  <text x="24" y="34" font-family="sans-serif" font-size="15" font-weight="700" fill="#0F172A">AI 辅助开发方法：人机协同与闭环验证</text>

  <!-- 4 阶段 -->
  <!-- 阶段 1: 人定范围 -->
  <g transform="translate(24, 54)">
    <rect width="144" height="110" rx="8" fill="#FAF5FF" stroke="#CBD5E1"/>
    <rect width="144" height="24" rx="8" fill="#E2E8F0"/>
    <text x="10" y="17" font-family="sans-serif" font-size="11" font-weight="700" fill="#0F172A">1. 需求与边界 (人)</text>
    <text x="10" y="44" font-family="sans-serif" font-size="12" font-weight="700" fill="#0F172A">明确业务目标</text>
    <text x="10" y="62" font-family="sans-serif" font-size="11" fill="#475569">梳理输入输出约束</text>
    <text x="10" y="80" font-family="sans-serif" font-size="11" fill="#475569">界定现场安全红线</text>
    <text x="10" y="98" font-family="monospace" font-size="9.5" fill="#64748B">制定测试用例初稿</text>
  </g>

  <path d="M 168 108 L 192 108" stroke="#D946EF" stroke-width="2"/>
  <polygon points="192,108 184,104 184,112" fill="#D946EF"/>

  <!-- 阶段 2: AI 辅助生成 -->
  <g transform="translate(194, 54)">
    <rect width="144" height="110" rx="8" fill="#FDF4FF" stroke="#D946EF"/>
    <rect width="144" height="24" rx="8" fill="#D946EF"/>
    <text x="10" y="17" font-family="sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">2. 辅助实现 (AI)</text>
    <text x="10" y="44" font-family="sans-serif" font-size="12" font-weight="700" fill="#D946EF">代码骨架生成</text>
    <text x="10" y="62" font-family="sans-serif" font-size="11" fill="#475569">业务状态机初版</text>
    <text x="10" y="80" font-family="sans-serif" font-size="11" fill="#475569">第三方接口逆向初探</text>
    <text x="10" y="98" font-family="monospace" font-size="9.5" fill="#D946EF">加速实现初稿</text>
  </g>

  <path d="M 338 108 L 362 108" stroke="#D946EF" stroke-width="2"/>
  <polygon points="362,108 354,104 354,112" fill="#D946EF"/>

  <!-- 阶段 3: 审查与修复 (闭环) -->
  <g transform="translate(364, 54)">
    <rect width="154" height="110" rx="8" fill="#ECFEFF" stroke="#0891B2" stroke-width="1.5"/>
    <rect width="154" height="24" rx="8" fill="#ECFEFF"/>
    <text x="10" y="17" font-family="sans-serif" font-size="11" font-weight="700" fill="#0891B2">3. 审查与修复 (人)</text>
    <text x="10" y="44" font-family="sans-serif" font-size="12" font-weight="700" fill="#0891B2">多批次连带缺陷复核</text>
    <text x="10" y="62" font-family="sans-serif" font-size="11" fill="#475569">防超额合并归一化</text>
    <text x="10" y="80" font-family="sans-serif" font-size="11" fill="#475569">回归测试断言验证</text>
    <text x="10" y="98" font-family="monospace" font-size="9.5" fill="#E02020">未过审 ⮌ 迭代修改</text>
  </g>

  <!-- 回退小环路 -->
  <path d="M 440 54 C 440 36, 266 36, 266 54" fill="none" stroke="#E02020" stroke-width="1.5" stroke-dasharray="3,3"/>
  <polygon points="266,54 262,46 270,46" fill="#E02020"/>
  <text x="350" y="40" font-family="sans-serif" font-size="9" fill="#E02020" text-anchor="middle">缺陷排查 / 反馈再修复</text>

  <path d="M 518 108 L 542 108" stroke="#34C759" stroke-width="2"/>
  <polygon points="542,108 534,104 534,112" fill="#34C759"/>

  <!-- 阶段 4: 证据分级 -->
  <g transform="translate(544, 54)">
    <rect width="152" height="110" rx="8" fill="#FAF5FF" stroke="#34C759"/>
    <rect width="152" height="24" rx="8" fill="#34C759"/>
    <text x="10" y="17" font-family="sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">4. 证据层级严格区分</text>
    <text x="10" y="44" font-family="sans-serif" font-size="11" font-weight="700" fill="#0F172A">① 本地单测通过</text>
    <text x="10" y="62" font-family="sans-serif" font-size="10.5" fill="#475569">证明逻辑自洽与用例覆盖</text>
    <text x="10" y="82" font-family="sans-serif" font-size="11" font-weight="700" fill="#0F172A">② 现场上线已验收</text>
    <text x="10" y="100" font-family="sans-serif" font-size="10.5" fill="#D946EF">证明多端协同满足生产需求</text>
  </g>

  <!-- 底部说明 -->
  <rect x="24" y="180" width="672" height="46" rx="6" fill="#FAF5FF"/>
  <text x="36" y="200" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#0F172A">核心工作原则：</text>
  <text x="120" y="200" font-family="sans-serif" font-size="11" fill="#475569">AI 负责快速生成初稿加速流程；人负责逻辑审查、安全红线与现场交付。代码实现与现场验收边界绝不混淆。</text>
  <text x="36" y="218" font-family="sans-serif" font-size="10.5" fill="#64748B">不把代码能跑当作生产成功，不在方案中承诺无依据的效率提升倍数。</text>
</svg>'''
    (VISUALS_DIR / "ai-workflow.svg").write_text(svg, encoding="utf-8")


def create_v10():
    # V10: simplehmi-path.svg (720x180) SimpleHmi 规范路径
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 180" width="100%" height="100%" role="img" aria-label="SimpleHmi 规范交付路径">
  <rect width="720" height="180" fill="#FAFCFD" rx="12"/>
  <rect x="10" y="10" width="700" height="160" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>

  <text x="24" y="32" font-family="sans-serif" font-size="14" font-weight="700" fill="#0F172A">SimpleHmi：从需求到可检查工业界面的规范路径</text>

  <g transform="translate(24, 48)">
    <rect width="144" height="76" rx="6" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">1. 需求卡片输入</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12" font-weight="600" fill="#0F172A">工位与操作约束</text>
    <text x="12" y="62" font-family="sans-serif" font-size="10.5" fill="#475569">状态定义 / 交互红线</text>
  </g>

  <path d="M 174 86 L 196 86" stroke="#D946EF" stroke-width="2"/>
  <polygon points="196,86 188,82 188,90" fill="#D946EF"/>

  <g transform="translate(198, 48)">
    <rect width="148" height="76" rx="6" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">2. 协议与状态机</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12" font-weight="600" fill="#0F172A">WebSocket 消息体</text>
    <text x="12" y="62" font-family="sans-serif" font-size="10.5" fill="#475569">统一数据包格式与心跳</text>
  </g>

  <path d="M 352 86 L 374 86" stroke="#D946EF" stroke-width="2"/>
  <polygon points="374,86 366,82 366,90" fill="#D946EF"/>

  <g transform="translate(376, 48)">
    <rect width="148" height="76" rx="6" fill="#FDF4FF" stroke="#D946EF"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">3. 开源样板实现</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12" font-weight="600" fill="#0F172A">React + TS 界面</text>
    <text x="12" y="62" font-family="sans-serif" font-size="10.5" fill="#475569">工业触屏组件范例</text>
  </g>

  <path d="M 530 86 L 552 86" stroke="#D946EF" stroke-width="2"/>
  <polygon points="552,86 544,82 544,90" fill="#D946EF"/>

  <g transform="translate(554, 48)">
    <rect width="142" height="76" rx="6" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">4. 检查与交付</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12" font-weight="600" fill="#0F172A">设计规范自检</text>
    <text x="12" y="62" font-family="sans-serif" font-size="10.5" fill="#475569">交付文档与开箱即用</text>
  </g>

  <text x="360" y="152" font-family="sans-serif" font-size="11" fill="#64748B" text-anchor="middle">工业软件轻量化原型规范 ｜ 代码开源于 GitHub</text>
</svg>'''
    (VISUALS_DIR / "simplehmi-path.svg").write_text(svg, encoding="utf-8")


def create_v11():
    # V11: foodmap-evidence.svg (720x180) 地图数据结构示意
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 180" width="100%" height="100%" role="img" aria-label="湖州美食地图数据结构与依据示意">
  <rect width="720" height="180" fill="#FAFCFD" rx="12"/>
  <rect x="10" y="10" width="700" height="160" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>

  <text x="24" y="32" font-family="sans-serif" font-size="14" font-weight="700" fill="#0F172A">湖州美食地图：数据结构与来源依据示意</text>

  <g transform="translate(24, 48)">
    <rect width="190" height="78" rx="6" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">1. 多源数据收集</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12" font-weight="600" fill="#0F172A">本地老饕推荐 / 笔记整理</text>
    <text x="12" y="64" font-family="sans-serif" font-size="10.5" fill="#475569">非商业推广，个人实测收录</text>
  </g>

  <path d="M 220 87 L 244 87" stroke="#D946EF" stroke-width="2"/>
  <polygon points="244,87 236,83 236,91" fill="#D946EF"/>

  <g transform="translate(246, 48)">
    <rect width="200" height="78" rx="6" fill="#FAF5FF" stroke="#E2E8F0"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">2. 结构化字段清洗</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12" font-weight="600" fill="#0F172A">名称 / 招牌 / 地址核实</text>
    <text x="12" y="64" font-family="sans-serif" font-size="10.5" fill="#475569">经纬度匹配与分类打标</text>
  </g>

  <path d="M 452 87 L 476 87" stroke="#D946EF" stroke-width="2"/>
  <polygon points="476,87 468,83 468,91" fill="#D946EF"/>

  <g transform="translate(478, 48)">
    <rect width="218" height="78" rx="6" fill="#FDF4FF" stroke="#D946EF"/>
    <text x="12" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#D946EF">3. 轻量交互呈现</text>
    <text x="12" y="44" font-family="sans-serif" font-size="12" font-weight="600" fill="#0F172A">移动端响应式地图卡片</text>
    <text x="12" y="64" font-family="sans-serif" font-size="10.5" fill="#475569">离线可用 / 快速检索</text>
  </g>

  <text x="360" y="152" font-family="sans-serif" font-size="11" fill="#64748B" text-anchor="middle">信息结构示意，不用于真实行车导航 ｜ 移动端单手交互探索项目</text>
</svg>'''
    (VISUALS_DIR / "foodmap-evidence.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    create_v01()
    create_v02()
    create_v03()
    create_v04()
    create_v05()
    create_v06()
    create_v09()
    create_v10()
    create_v11()
    print("全部 SVG 矢量素材生成完毕！")
