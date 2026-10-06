/**
 * 2、3、4 页面双图层联动切换引擎 (Multi-layer Sticky Pinning Engine)
 * 效果：鼠标下滑时下图层（全幅背景）跟随滚动，上图层（文字+悬浮卡片）固定在视口，在背景切换时平滑更新文本与视觉
 */
(function() {
  'use strict';

  var stage = document.getElementById('showcase-stage');
  if (!stage) return;

  var pinnedYear = document.getElementById('pinned-year');
  var pinnedTitle = document.getElementById('pinned-title');
  var pinnedLead = document.getElementById('pinned-lead');
  var pinnedCategory = document.getElementById('pinned-category');
  var pinnedFacts = document.getElementById('pinned-facts');
  var floatingCardImg = document.getElementById('floating-card-img');
  var floatingCardTitle = document.getElementById('floating-card-title');
  var floatingCardCaption = document.getElementById('floating-card-caption');
  var floatingCardStatus = document.getElementById('floating-card-status');
  var pinnedContainer = document.querySelector('.showcase-pinned-overlay');

  var PROJECTS = [
    {
      year: '2020',
      title: '考亭古街',
      category: 'COMMERCIAL DEFINITION',
      lead: '面对混沌非标诉求，坚决不被杂音带偏。提炼“文旅溯源地”唯一成立主线，售前主创推动 212 万元合同签署与回款闭环。',
      tags: ['合同金额 212 万元', '售前策划主创', '多轮高层汇报立项'],
      cardTitle: 'KAOTING · TOP STRATEGY',
      cardImg: 'assets/images/kaoting.jpg',
      cardCaption: '福建建阳考亭古街：落地实景与文脉溯源空间',
      cardStatus: '已立项交付'
    },
    {
      year: '2024',
      title: '数字月台',
      category: 'INDUSTRIAL HMI & CONTROL',
      lead: '多终端工业中控状态机，打通真实 PLC 与移动机器人硬件协议。单兵解决多工位冲突与异常断线，100% No-Mock 真实联调。',
      tags: ['生产环境已上线已验收', '订单全局状态机', 'Fastify · React · PLC'],
      cardTitle: 'DIGITAL DOCK · CONTROL SPEC',
      cardImg: 'assets/visuals/dock-system.svg',
      cardCaption: '工业中控职责边界拓扑（调度层 ↔ 中控 ↔ PLC 控制器）',
      cardStatus: '生产环境运行中'
    },
    {
      year: '2025',
      title: 'EmergentInc',
      category: 'AI-NATIVE AUTONOMOUS SYSTEM',
      lead: '让 AI 走出对话框。开源自主智能体系统，打通 4 链 USDT 自动核销、pure-ast-json 纯 AST 安全沙箱与持久区自进化。',
      tags: ['开源自主系统架构', '4 链 USDT 自动核销', '纯 AST 安全沙箱'],
      cardTitle: 'EMERGENTINC · AUTONOMOUS AGENT',
      cardImg: 'assets/images/emergentinc.png',
      cardCaption: '智能体自主经营全景（商城销售 · 基因谱系 · 链上核销）',
      cardStatus: '开源代码库就绪'
    }
  ];

  var activeIndex = -1;
  var isTransitioning = false;

  function updateContent(index) {
    if (index === activeIndex || isTransitioning) return;
    activeIndex = index;
    var data = PROJECTS[index];
    if (!data) return;

    // 添加平滑淡出过渡
    pinnedContainer.classList.add('is-switching');

    setTimeout(function() {
      if (pinnedYear) pinnedYear.textContent = data.year;
      if (pinnedTitle) pinnedTitle.textContent = data.title;
      if (pinnedCategory) pinnedCategory.textContent = data.category;
      if (pinnedLead) pinnedLead.textContent = data.lead;

      if (pinnedFacts) {
        pinnedFacts.innerHTML = '';
        data.tags.forEach(function(tag) {
          var span = document.createElement('span');
          span.className = 'fact-tag';
          span.textContent = tag;
          pinnedFacts.appendChild(span);
        });
      }

      if (floatingCardImg) floatingCardImg.src = data.cardImg;
      if (floatingCardTitle) floatingCardTitle.textContent = data.cardTitle;
      if (floatingCardCaption) floatingCardCaption.textContent = data.cardCaption;
      if (floatingCardStatus) floatingCardStatus.textContent = data.cardStatus;

      pinnedContainer.classList.remove('is-switching');
    }, 180);
  }

  function onScroll() {
    var rect = stage.getBoundingClientRect();
    var windowH = window.innerHeight;

    // 计算滚入位置
    var scrolled = -rect.top;
    if (scrolled < 0) {
      updateContent(0);
      return;
    }

    var progress = scrolled / windowH;
    var index = Math.min(2, Math.max(0, Math.floor(progress + 0.38)));
    updateContent(index);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  // 初始化渲染
  updateContent(0);
})();
