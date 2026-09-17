/**
 * 《信号志 · SIGNAL》Layer 3 · 赛博工控信号拓扑场（Cyber-Industrial Signal Topology）
 *
 * 在可激发介质元胞自动机（Excitable Medium CA）基础上深度升级：
 * 1. 白炽光核 + 双层霓虹辉光（White-Hot Core & Dual Glow）：峰值能量附带白炽高光与外晕扩散。
 * 2. 瞬态总线脉冲（Circuit Bus Surge）：爆发时沿网格正交轴线疾驰出高速激光走线与数据导通。
 * 3. 爆发规线准星（Swiss Target Reticle）：爆发起点瞬现精密瑞士规线与机器视觉对焦十字。
 * 4. 双色套印干涉（Overprint Interference）：洋红与青色波纹碰撞处触发高能电光紫共振。
 * 5. 全局指尖交互（Cursor Ionization & Click Burst）：光标滑过点阵微弱电离，点击屏幕引爆十字总线脉冲。
 *
 * 工程纪律：
 * 1. prefers-reduced-motion: reduce 时不启动。
 * 2. 移动端 (window.innerWidth <= 768) 不执行（省电省性能）。
 * 3. 页面隐藏 (document.hidden) 时自动暂停 requestAnimationFrame。
 * 4. 格点严格吸附 12px 点阵网格（与 Layer 1 底纹对齐）。
 * 5. 定长 TypedArray 与活跃索引池，同屏活跃上限严格管控，零外部库依赖。
 */
(function () {
  'use strict';

  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return;
  }
  if (window.innerWidth <= 768) {
    return;
  }

  const canvas = document.getElementById('signal-field');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  // ── 核心常量配置 ─────────────────────────────────────────
  const CELL = 12;                         // 与 Layer 1 点阵严格 12px 对齐
  const COLORS = [
    '#d946ef', // 1: 霓虹洋红 (Magenta)
    '#0891b2', // 2: 电光青 (Cyan)
    '#8b5cf6'  // 3: 套印电光紫 (Overprint Violet)
  ];
  const MAX_OUTBREAKS = 3;                 // 自动爆发最大并发源
  const MAX_ACTIVE = 900;                  // 活跃格上限
  const MAX_BUS = 12;                      // 最大并发总线脉冲
  const MAX_RETICLES = 6;                  // 最大并发准星标记
  const SPREAD_PROB = 0.84;                // 8 邻域感染基准概率
  const STEP_MS = 85;                      // CA 扩散波进间隔 (ms)
  const DECAY_PER_MS = 0.00062;            // 能量线性衰减速度 (~1.6s 熄灭)

  let width = 0, height = 0, dpr = 1;
  let cols = 0, rows = 0;
  let intensity = null;   // Float32Array：能量强度 (0.0 ~ 1.0)
  let cellColor = null;   // Uint8Array：颜色索引 (0=无, 1=洋红, 2=青, 3=套印紫)
  let activeList = [];    // 活跃格索引数组 (快速迭代与删除)

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cols = Math.ceil(width / CELL) + 1;
    rows = Math.ceil(height / CELL) + 1;
    intensity = new Float32Array(cols * rows);
    cellColor = new Uint8Array(cols * rows);
    activeList = [];
    frontier = [];
    busPulses = [];
    reticles = [];
  }
  window.addEventListener('resize', resize, { passive: true });
  resize();

  // ── 数据结构：前沿、准星、总线脉冲 ─────────────────────────
  let frontier = [];      // 待扩散前沿：[x, y, colorIdx, dist]
  let busPulses = [];     // 走线脉冲：{ sx, sy, cx, cy, dx, dy, steps, maxSteps, colorIdx, stepTimer }
  let reticles = [];      // 爆发准星：{ x, y, colorIdx, birth, life }
  let lastSpawn = performance.now();
  let nextSpawn = 1200 + Math.random() * 1400; // 1.2–2.6s 自动爆发一次
  let outbreakCount = 0;
  let clickColorIdx = 0;  // 鼠标交互颜色交替 (0: 洋红, 1: 青)

  // 格点点燃函数（包含双色碰撞干涉判定）
  function ignite(x, y, colorIdx, strength, forceOverprint = false) {
    if (x < 0 || y < 0 || x >= cols || y >= rows) return false;
    const idx = y * cols + x;
    const curCol = cellColor[idx];

    // 碰撞干涉：如果已激发且为不同颜色，转为套印紫色并重注能量
    if (curCol !== 0) {
      if ((curCol !== colorIdx + 1 && curCol !== 3) || forceOverprint) {
        cellColor[idx] = 3; // 3: 套印紫
        intensity[idx] = Math.min(1.0, intensity[idx] + 0.55);
        // 干涉点有概率激发出一条短脉冲
        if (Math.random() < 0.4 && busPulses.length < MAX_BUS) {
          const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
          const [dx, dy] = dirs[Math.floor(Math.random() * dirs.length)];
          addBusPulse(x, y, 2, dx, dy, Math.floor(6 + Math.random() * 6));
        }
        return true;
      }
      return false; // 同色已活跃，不重复感染
    }

    if (activeList.length >= MAX_ACTIVE) return false;
    cellColor[idx] = colorIdx + 1;
    intensity[idx] = strength;
    activeList.push(idx);
    return true;
  }

  // 增加爆发十字准星与规线
  function addReticle(gx, gy, colorIdx) {
    if (reticles.length >= MAX_RETICLES) reticles.shift();
    reticles.push({
      x: gx * CELL,
      y: gy * CELL,
      colorIdx: colorIdx,
      birth: performance.now(),
      life: 280 // 280ms
    });
  }

  // 增加正交总线脉冲
  function addBusPulse(gx, gy, colorIdx, dx, dy, maxSteps) {
    if (busPulses.length >= MAX_BUS) busPulses.shift();
    busPulses.push({
      cx: gx,
      cy: gy,
      dx: dx,
      dy: dy,
      steps: 0,
      maxSteps: maxSteps,
      colorIdx: colorIdx,
      lastTick: performance.now()
    });
  }

  // 爆发源触发
  function spawnOutbreak(gx = null, gy = null, chosenColor = null, isUser = false) {
    if (!isUser && outbreakCount >= MAX_OUTBREAKS) return;
    if (activeList.length > MAX_ACTIVE * 0.75 && !isUser) return;

    const x = gx !== null ? gx : Math.floor(Math.random() * (cols - 4)) + 2;
    const y = gy !== null ? gy : Math.floor(Math.random() * (rows - 4)) + 2;
    const colorIdx = chosenColor !== null ? chosenColor : Math.floor(Math.random() * 2);

    ignite(x, y, colorIdx, 1.0);
    frontier.push([x, y, colorIdx, 0]);
    addReticle(x, y, colorIdx);

    if (isUser) {
      // 用户点击：四向全爆发总线脉冲
      const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
      for (let i = 0; i < 4; i++) {
        addBusPulse(x, y, colorIdx, dirs[i][0], dirs[i][1], Math.floor(10 + Math.random() * 8));
      }
    } else {
      outbreakCount++;
      // 自然爆发：有 50% 概率发射 1~2 条高速总线走线
      if (Math.random() < 0.6) {
        const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        const [dx, dy] = dirs[Math.floor(Math.random() * dirs.length)];
        addBusPulse(x, y, colorIdx, dx, dy, Math.floor(8 + Math.random() * 8));
      }
    }
  }

  // CA 扩散步进
  function spreadStep() {
    if (frontier.length === 0) {
      outbreakCount = 0;
      return;
    }
    const next = [];
    for (let i = 0; i < frontier.length; i++) {
      const [x, y, colorIdx, dist] = frontier[i];
      const childStrength = Math.max(0.24, 1.0 - (dist + 1) * 0.058);
      let infected = 0;

      for (let dy = -1; dy <= 1; dy++) {
        for (let dx = -1; dx <= 1; dx++) {
          if (dx === 0 && dy === 0) continue;
          if (Math.random() > SPREAD_PROB) continue;
          // 对角减速，保持近似圆弧
          if (dx !== 0 && dy !== 0 && Math.random() > 0.68) continue;

          const nx = x + dx;
          const ny = y + dy;
          if (ignite(nx, ny, colorIdx, childStrength)) {
            next.push([nx, ny, colorIdx, dist + 1]);
            infected++;
          }
        }
      }
    }
    frontier = next;
    if (frontier.length === 0) outbreakCount = 0;
  }

  // ── 总线脉冲移动更新 ───────────────────────────────────────
  const BUS_TICK_MS = 28; // 每 28ms 前进一格，营造高速电光感
  function updateBusPulses(now) {
    for (let i = busPulses.length - 1; i >= 0; i--) {
      const p = busPulses[i];
      if (now - p.lastTick >= BUS_TICK_MS) {
        p.lastTick = now;
        p.cx += p.dx;
        p.cy += p.dy;
        p.steps++;

        if (p.cx < 0 || p.cx >= cols || p.cy < 0 || p.cy >= rows || p.steps >= p.maxSteps) {
          busPulses.splice(i, 1);
          continue;
        }

        // 点亮沿途格点
        ignite(p.cx, p.cy, p.colorIdx, 0.95);
      }
    }
  }

  // ── 交互监听：光标电离与点击引爆 ───────────────────────────
  let lastMouseGx = -1;
  let lastMouseGy = -1;
  let lastMoveTime = 0;

  function onPointerMove(e) {
    const now = performance.now();
    if (now - lastMoveTime < 32) return; // 节流控制 (~30fps)
    lastMoveTime = now;

    const mgx = Math.round(e.clientX / CELL);
    const mgy = Math.round(e.clientY / CELL);

    if (mgx === lastMouseGx && mgy === lastMouseGy) return;
    lastMouseGx = mgx;
    lastMouseGy = mgy;

    // 在鼠标周围 2 格内激发出低强度微光晕
    const hoverColor = (mgx + mgy) % 2;
    for (let dy = -1; dy <= 1; dy++) {
      for (let dx = -1; dx <= 1; dx++) {
        if (Math.random() < 0.6) {
          ignite(mgx + dx, mgy + dy, hoverColor, 0.36);
        }
      }
    }
  }

  function onPointerDown(e) {
    // 忽略右键点击
    if (e.button !== 0 && e.button !== undefined) return;
    const mgx = Math.round(e.clientX / CELL);
    const mgy = Math.round(e.clientY / CELL);
    spawnOutbreak(mgx, mgy, clickColorIdx, true);
    clickColorIdx = (clickColorIdx + 1) % 2;
  }

  window.addEventListener('pointermove', onPointerMove, { passive: true });
  window.addEventListener('pointerdown', onPointerDown, { passive: true });

  // ── 主渲染循环 ─────────────────────────────────────────────
  let isRunning = true;
  let animId = null;
  let lastFrame = performance.now();
  let lastStep = performance.now();

  function loop(now) {
    if (!isRunning) return;
    const dt = Math.min(now - lastFrame, 80);
    lastFrame = now;

    // 调度自然爆发
    if (now - lastSpawn > nextSpawn) {
      spawnOutbreak();
      lastSpawn = now;
      nextSpawn = 1200 + Math.random() * 1500;
    }

    // CA 步进
    if (now - lastStep > STEP_MS) {
      spreadStep();
      lastStep = now;
    }

    // 更新高速总线
    updateBusPulses(now);

    // 清屏
    ctx.clearRect(0, 0, width, height);

    // 1. 绘制高速总线激光连线 (底层)
    if (busPulses.length > 0) {
      for (let i = 0; i < busPulses.length; i++) {
        const p = busPulses[i];
        const hx = p.cx * CELL;
        const hy = p.cy * CELL;
        const tailLen = Math.min(p.steps, 4) * CELL;
        const tx = hx - p.dx * tailLen;
        const ty = hy - p.dy * tailLen;

        ctx.strokeStyle = COLORS[p.colorIdx];
        ctx.lineWidth = 1.5;
        ctx.globalAlpha = 0.75;
        ctx.beginPath();
        ctx.moveTo(tx, ty);
        ctx.lineTo(hx, hy);
        ctx.stroke();

        // 走线头部高亮光标
        ctx.fillStyle = '#ffffff';
        ctx.globalAlpha = 0.95;
        ctx.fillRect(hx - 2, hy - 2, 4, 4);
      }
    }

    // 2. 绘制活跃格点（包含高光白芯与外层霓虹辉光）
    for (let i = activeList.length - 1; i >= 0; i--) {
      const idx = activeList[i];
      intensity[idx] -= DECAY_PER_MS * dt;

      if (intensity[idx] <= 0) {
        intensity[idx] = 0;
        cellColor[idx] = 0;
        activeList[i] = activeList[activeList.length - 1];
        activeList.pop();
        continue;
      }

      const x = (idx % cols) * CELL;
      const y = Math.floor(idx / cols) * CELL;
      const t = intensity[idx];
      const colIdx = cellColor[idx] - 1;
      const color = COLORS[colIdx] || COLORS[0];

      if (t > 0.6) {
        // [高能态]：外层柔和晕影 + 中层高纯度方块 + 中心白炽核
        // 外层晕影
        const glow = 8 + t * 4; // 10–12px
        ctx.globalAlpha = t * 0.22;
        ctx.fillStyle = color;
        ctx.fillRect(x - glow / 2, y - glow / 2, glow, glow);

        // 主体色块
        const size = 3 + t * 3.8; // 5–7px
        ctx.globalAlpha = Math.min(1.0, t * 0.95);
        ctx.fillRect(x - size / 2, y - size / 2, size, size);

        // 纯白高能光核 (White-Hot Core)
        const core = 2;
        ctx.globalAlpha = Math.min(1.0, (t - 0.55) * 2.2);
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(x - core / 2, y - core / 2, core, core);
      } else if (t > 0.22) {
        // [中等态]：清晰锐利的信号方块 (3–5px)
        const size = 2 + t * 3.5;
        ctx.globalAlpha = t * 0.88;
        ctx.fillStyle = color;
        ctx.fillRect(x - size / 2, y - size / 2, size, size);
      } else {
        // [衰减尾声]：严格贴合网格的微小亮点 (2px)
        ctx.globalAlpha = t * 0.75;
        ctx.fillStyle = color;
        ctx.fillRect(x - 1, y - 1, 2, 2);
      }
    }

    // 3. 绘制爆发规线准星 (瑞士工程对焦标记)
    if (reticles.length > 0) {
      for (let i = reticles.length - 1; i >= 0; i--) {
        const r = reticles[i];
        const age = now - r.birth;
        if (age >= r.life) {
          reticles.splice(i, 1);
          continue;
        }

        const progress = age / r.life;
        const alpha = (1 - progress) * 0.95;
        const rad = 4 + progress * 10; // 从 4px 扩张到 14px
        const color = COLORS[r.colorIdx] || COLORS[0];

        ctx.strokeStyle = color;
        ctx.lineWidth = 1;
        ctx.globalAlpha = alpha;

        // 十字断线规线 (+)
        ctx.beginPath();
        // 垂直两段
        ctx.moveTo(r.x, r.y - rad);
        ctx.lineTo(r.x, r.y - rad * 0.35);
        ctx.moveTo(r.x, r.y + rad * 0.35);
        ctx.lineTo(r.x, r.y + rad);
        // 水平两段
        ctx.moveTo(r.x - rad, r.y);
        ctx.lineTo(r.x - rad * 0.35, r.y);
        ctx.moveTo(r.x + rad * 0.35, r.y);
        ctx.lineTo(r.x + rad, r.y);
        ctx.stroke();

        // 四角直角标定框
        const b = rad * 0.75;
        const d = 2.5;
        ctx.beginPath();
        // 左上
        ctx.moveTo(r.x - b, r.y - b + d);
        ctx.lineTo(r.x - b, r.y - b);
        ctx.lineTo(r.x - b + d, r.y - b);
        // 右上
        ctx.moveTo(r.x + b - d, r.y - b);
        ctx.lineTo(r.x + b, r.y - b);
        ctx.lineTo(r.x + b, r.y - b + d);
        // 右下
        ctx.moveTo(r.x + b, r.y + b - d);
        ctx.lineTo(r.x + b, r.y + b);
        ctx.lineTo(r.x + b - d, r.y + b);
        // 左下
        ctx.moveTo(r.x - b + d, r.y + b);
        ctx.lineTo(r.x - b, r.y + b);
        ctx.lineTo(r.x - b, r.y + b - d);
        ctx.stroke();
      }
    }

    ctx.globalAlpha = 1.0;
    animId = requestAnimationFrame(loop);
  }

  // 页面可见性管理
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
      isRunning = false;
      if (animId) cancelAnimationFrame(animId);
    } else if (!isRunning) {
      isRunning = true;
      lastFrame = performance.now();
      lastSpawn = performance.now();
      lastStep = performance.now();
      animId = requestAnimationFrame(loop);
    }
  });

  animId = requestAnimationFrame(loop);
})();
