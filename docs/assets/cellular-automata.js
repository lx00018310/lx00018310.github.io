/**
 * 首页专属背景 · 极简纯黑元胞自动机离散点阵演化 (Cellular Automata - Conway's Game of Life)
 * 
 * 设计规范：
 * 1. 纯黑圆点，严格吸附 12px 背景点阵网格，中心对齐 (col * 12 + 6, row * 12 + 6)。
 * 2. 零发光、零连线、零描边、零模糊、零鼠标交互。
 * 3. 240ms 演化步进（移动端 320ms），requestAnimationFrame 平滑渲染。
 * 4. 初始种子为偏左上区域小型随机簇 + Glider 混合播种。
 * 5. 存活细胞数低于阈值时触发冷却保护型轻干预补种，系统自运行不熄灭。
 * 6. 支持 prefers-reduced-motion 与页面后台自动挂起。
 */
(function () {
  'use strict';

  const canvas = document.getElementById('cellular-automata-field');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  const isReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── 配置参数 ─────────────────────────────────────────
  const CONFIG = {
    cell: 12,                  // 严格对齐 CSS 点阵 12px 网格
    dotRadius: 1.4,            // 元胞小圆点半径 (px)
    aliveAlpha: 0.62,          // 桌面端活细胞纯黑透明度
    mobileAliveAlpha: 0.48,    // 移动端活细胞纯黑透明度
    stepInterval: 240,         // 桌面端演化步进周期 (ms)
    mobileStepInterval: 320,   // 移动端演化步进周期 (ms)
    minAliveThreshold: 12,     // 最低存活细胞阈值（触发补种）
    reseedCooldown: 5000,      // 补种冷却时间 (ms)
    clusterRadius: 3,          // 种子簇半径 (格)
    clusterDensity: 0.45       // 种子簇密度
  };

  let width = 0, height = 0, dpr = 1;
  let cols = 0, rows = 0;
  let isMobile = false;
  let currentGrid = null;
  let nextGrid = null;
  let lastStepTime = 0;
  let lastSeedTime = 0;
  let isRunning = true;
  let animId = null;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;
    isMobile = width <= 768;

    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    cols = Math.ceil(width / CONFIG.cell) + 1;
    rows = Math.ceil(height / CONFIG.cell) + 1;

    currentGrid = new Uint8Array(cols * rows);
    nextGrid = new Uint8Array(cols * rows);

    initSeed();
  }

  // ── 播种模式 ─────────────────────────────────────────
  // 标准滑翔机 (Glider) 模式
  const GLIDER = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
  ];

  function placePattern(pattern, startX, startY) {
    for (let r = 0; r < pattern.length; r++) {
      for (let c = 0; c < pattern[r].length; c++) {
        if (pattern[r][c] === 1) {
          const gx = startX + c;
          const gy = startY + r;
          if (gx >= 0 && gx < cols && gy >= 0 && gy < rows) {
            currentGrid[gy * cols + gx] = 1;
          }
        }
      }
    }
  }

  function placeRandomCluster(cx, cy, radius, density) {
    for (let dy = -radius; dy <= radius; dy++) {
      for (let dx = -radius; dx <= radius; dx++) {
        if (dx * dx + dy * dy <= radius * radius) {
          if (Math.random() < density) {
            const gx = cx + dx;
            const gy = cy + dy;
            if (gx >= 0 && gx < cols && gy >= 0 && gy < rows) {
              currentGrid[gy * cols + gx] = 1;
            }
          }
        }
      }
    }
  }

  function initSeed() {
    currentGrid.fill(0);
    // 偏左上方（约 35% 宽、32% 高处），避开正中心大标题，给与理性启动源
    const cx = Math.floor(cols * 0.35);
    const cy = Math.floor(rows * 0.32);

    placeRandomCluster(cx, cy, CONFIG.clusterRadius, CONFIG.clusterDensity);
    placePattern(GLIDER, cx + 5, cy + 2);

    lastSeedTime = performance.now();
  }

  function tryReseed(now, aliveCount) {
    if (aliveCount >= CONFIG.minAliveThreshold) return;
    if (now - lastSeedTime < CONFIG.reseedCooldown) return;

    // 轻量补种：在中心偏外围区域注入新的微型种子
    const rx = Math.floor(cols * (0.25 + Math.random() * 0.5));
    const ry = Math.floor(rows * (0.2 + Math.random() * 0.4));
    
    if (Math.random() < 0.5) {
      placePattern(GLIDER, rx, ry);
    } else {
      placeRandomCluster(rx, ry, 2, 0.4);
    }
    lastSeedTime = now;
  }

  // ── 生命游戏演化规则 ──────────────────────────────────
  function stepSimulation() {
    let aliveCount = 0;

    for (let y = 0; y < rows; y++) {
      const rowOffset = y * cols;
      for (let x = 0; x < cols; x++) {
        let neighbors = 0;

        for (let dy = -1; dy <= 1; dy++) {
          const ny = y + dy;
          if (ny < 0 || ny >= rows) continue;
          const nRowOffset = ny * cols;

          for (let dx = -1; dx <= 1; dx++) {
            if (dx === 0 && dy === 0) continue;
            const nx = x + dx;
            if (nx < 0 || nx >= cols) continue;

            if (currentGrid[nRowOffset + nx] === 1) {
              neighbors++;
            }
          }
        }

        const idx = rowOffset + x;
        const isAlive = currentGrid[idx] === 1;

        if (isAlive) {
          if (neighbors === 2 || neighbors === 3) {
            nextGrid[idx] = 1;
            aliveCount++;
          } else {
            nextGrid[idx] = 0;
          }
        } else {
          if (neighbors === 3) {
            nextGrid[idx] = 1;
            aliveCount++;
          } else {
            nextGrid[idx] = 0;
          }
        }
      }
    }

    // 双缓冲交换
    const temp = currentGrid;
    currentGrid = nextGrid;
    nextGrid = temp;

    return aliveCount;
  }

  // ── 渲染 ─────────────────────────────────────────────
  function draw() {
    ctx.clearRect(0, 0, width, height);

    const alpha = isMobile ? CONFIG.mobileAliveAlpha : CONFIG.aliveAlpha;
    ctx.fillStyle = `rgba(0, 0, 0, ${alpha})`;

    ctx.beginPath();
    const halfCell = CONFIG.cell / 2; // 6px，中心与 background-image 严格重叠
    const r = CONFIG.dotRadius;
    const twoPi = Math.PI * 2;

    for (let y = 0; y < rows; y++) {
      const rowOffset = y * cols;
      const cy = y * CONFIG.cell + halfCell;
      for (let x = 0; x < cols; x++) {
        if (currentGrid[rowOffset + x] === 1) {
          const cx = x * CONFIG.cell + halfCell;
          ctx.moveTo(cx + r, cy);
          ctx.arc(cx, cy, r, 0, twoPi);
        }
      }
    }
    ctx.fill();
  }

  // ── 主循环 ───────────────────────────────────────────
  function loop(now) {
    if (!isRunning) return;

    const interval = isMobile ? CONFIG.mobileStepInterval : CONFIG.stepInterval;
    if (now - lastStepTime >= interval) {
      const aliveCount = stepSimulation();
      tryReseed(now, aliveCount);
      lastStepTime = now;
      draw();
    }

    animId = requestAnimationFrame(loop);
  }

  // ── 事件监听与生命周期 ─────────────────────────────────
  window.addEventListener('resize', () => {
    resize();
    draw();
  }, { passive: true });

  document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
      isRunning = false;
      if (animId) cancelAnimationFrame(animId);
    } else if (!isRunning) {
      isRunning = true;
      lastStepTime = performance.now();
      animId = requestAnimationFrame(loop);
    }
  });

  // 初始化
  resize();
  draw();

  // 若开启无障碍减弱动态效果，仅渲染静态初始种子，不启动步进循环
  if (!isReducedMotion) {
    lastStepTime = performance.now();
    animId = requestAnimationFrame(loop);
  }
})();
