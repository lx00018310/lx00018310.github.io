/**
 * 首页棋盘视口专属 · 元胞自动机生灭演化 (Cellular Automata Engine)
 * 专为首屏镂空棋盘视口定制，6px 高精网格驱动
 * 特性：
 * 1. 初始化以 Bahnschrift / DIN 工业字形采样呈现「Cellular Automaton / Conway's Game of Life / 1970」；
 * 2. 动效时间线：1s 主题紫色 -> 1s 电光青色 -> 1s 霓虹热红 -> 1s 科技电蓝 -> 1s 极境纯白 (总计 5s 静态赛博朋克文字)；
 * 3. 5s 后正式进入康威生命游戏生灭自主演化。
 */
(function() {
  'use strict';

  var canvas = document.getElementById('hero-cellular-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  if (!ctx) return;

  var container = canvas.parentElement;
  var width = 0, height = 0, dpr = 1;
  var cellSize = 6; // 6px 高精网格
  var cols = 0, rows = 0;
  var grid = null, nextGrid = null;
  var lastStep = 0;
  var stepInterval = 120; // 120ms 步进
  var animId = null;
  var isVisible = false;
  var isRunning = false;
  var pausedAt = null;
  var renderInterval = 1000 / 30;
  var lastRender = -Infinity;
  var lastColorKey = '';
  var needsRender = true;
  var dotCanvas = document.createElement('canvas');
  var dotCtx = dotCanvas.getContext('2d');
  var dotSize = 0;
  var dotColorKey = '';
  var dotDpr = 0;

  // 动效时间轴参数（总冻结期 5000ms：1s 紫色定格 + 3s 渐变转白 + 1s 白色定格）
  var freezeDuration = 5000;
  var freezeStartTime = 0;
  var freezeUntil = 0;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = container.clientWidth || 1200;
    height = container.clientHeight || 560;

    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    cols = Math.ceil(width / cellSize);
    rows = Math.ceil(height / cellSize);

    grid = new Uint8Array(cols * rows);
    nextGrid = new Uint8Array(cols * rows);

    var now = performance.now();
    var animationNow = pausedAt === null ? now : pausedAt;
    // 在 5 秒冻结期内或首次进入时，重置并采样文字
    if (freezeUntil === 0 || animationNow < freezeUntil) {
      freezeStartTime = now;
      freezeUntil = freezeStartTime + freezeDuration;
      seedText();
    } else {
      seedRandom();
    }
    if (pausedAt !== null) pausedAt = now;
    needsRender = true;
    lastRender = -Infinity;
  }

  /**
   * 采用 Bahnschrift / DIN 工业字体对文字进行高精度 6px 点阵采样
   */
  function seedText() {
    grid.fill(0);
    var offCanvas = document.createElement('canvas');
    offCanvas.width = width;
    offCanvas.height = height;
    var offCtx = offCanvas.getContext('2d');
    if (!offCtx) return;

    // 清除透明画布，未绘制区域保持 RGBA(0, 0, 0, 0)
    offCtx.clearRect(0, 0, width, height);

    var line1 = "Cellular Automaton";
    var line2 = "Conway's Game of Life";
    var line3 = "1970";

    // 严格限制最大宽度在画布宽度的 90% 以内
    var maxW = Math.floor(width * 0.90);
    var fontFamily = '"Bahnschrift", "DIN Alternate", "DIN", "Segoe UI Semibold", sans-serif';

    // 动态二分逼近适合字号
    var low = 16, high = Math.min(Math.floor(height * 0.38), 200);
    var bestF2 = 64;
    while (low <= high) {
      var mid = Math.floor((low + high) / 2);
      offCtx.font = '700 ' + mid + 'px ' + fontFamily;
      var textW = offCtx.measureText(line2).width;
      if (textW <= maxW) {
        bestF2 = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    var f2Size = bestF2;
    var f1Size = Math.max(Math.floor(f2Size * 0.70), 14);
    var f3Size = Math.max(Math.floor(f2Size * 0.65), 14);
    var spacing = Math.floor(f2Size * 0.22);
    var totalH = f1Size + f2Size + f3Size + spacing * 2;

    // 若总高度超出画框安全区域 (85% 视口高度)，等比例自适应缩放
    if (totalH > height * 0.85) {
      var scale = (height * 0.85) / totalH;
      f2Size = Math.floor(f2Size * scale);
      f1Size = Math.max(Math.floor(f2Size * 0.70), 14);
      f3Size = Math.max(Math.floor(f2Size * 0.65), 14);
      spacing = Math.floor(f2Size * 0.22);
      totalH = f1Size + f2Size + f3Size + spacing * 2;
    }

    var startY = Math.floor((height - totalH) / 2);

    // 显式基线与居中对齐
    offCtx.textBaseline = 'middle';
    offCtx.textAlign = 'center';
    offCtx.fillStyle = '#ffffff';

    var y1 = startY + f1Size * 0.5;
    var y2 = y1 + f1Size * 0.5 + spacing + f2Size * 0.5;
    var y3 = y2 + f2Size * 0.5 + spacing + f3Size * 0.5;

    offCtx.font = '700 ' + f1Size + 'px ' + fontFamily;
    offCtx.fillText(line1, width / 2, y1);

    offCtx.font = '700 ' + f2Size + 'px ' + fontFamily;
    offCtx.fillText(line2, width / 2, y2);

    offCtx.font = '700 ' + f3Size + 'px ' + fontFamily;
    offCtx.fillText(line3, width / 2, y3);

    // 读取像素数据进行元胞中心与边缘采样
    var imgData = offCtx.getImageData(0, 0, width, height).data;
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        var cx = Math.floor(c * cellSize + cellSize * 0.5);
        var cy = Math.floor(r * cellSize + cellSize * 0.5);
        if (cx < width && cy < height) {
          var hits = 0;
          var samplePts = [
            [cx, cy],
            [cx - 1, cy],
            [cx + 1, cy],
            [cx, cy - 1],
            [cx, cy + 1]
          ];
          for (var k = 0; k < samplePts.length; k++) {
            var sx = samplePts[k][0];
            var sy = samplePts[k][1];
            if (sx >= 0 && sx < width && sy >= 0 && sy < height) {
              var idx = (sy * width + sx) * 4;
              var red = imgData[idx];
              var alpha = imgData[idx + 3];
              if (red > 80 && alpha > 80) {
                hits++;
              }
            }
          }
          if (hits >= 2) {
            grid[r * cols + c] = 1;
          }
        }
      }
    }
  }

  function seedRandom() {
    grid.fill(0);
    var clusterCount = Math.max(16, Math.floor((cols * rows) / 450));
    for (var i = 0; i < clusterCount; i++) {
      var cx = Math.floor(Math.random() * cols);
      var cy = Math.floor(Math.random() * rows);
      var radius = 5;
      for (var dy = -radius; dy <= radius; dy++) {
        for (var dx = -radius; dx <= radius; dx++) {
          if (dx * dx + dy * dy <= radius * radius && Math.random() < 0.46) {
            var gx = (cx + dx + cols) % cols;
            var gy = (cy + dy + rows) % rows;
            grid[gy * cols + gx] = 1;
          }
        }
      }
    }
  }

  function countNeighbors(x, y) {
    var count = 0;
    for (var dy = -1; dy <= 1; dy++) {
      for (var dx = -1; dx <= 1; dx++) {
        if (dx === 0 && dy === 0) continue;
        var nx = (x + dx + cols) % cols;
        var ny = (y + dy + rows) % rows;
        count += grid[ny * cols + nx];
      }
    }
    return count;
  }

  function step() {
    var alive = 0;
    for (var y = 0; y < rows; y++) {
      for (var x = 0; x < cols; x++) {
        var idx = y * cols + x;
        var n = countNeighbors(x, y);
        var state = grid[idx];
        if (state === 1 && (n === 2 || n === 3)) {
          nextGrid[idx] = 1;
          alive++;
        } else if (state === 0 && n === 3) {
          nextGrid[idx] = 1;
          alive++;
        } else {
          nextGrid[idx] = 0;
        }
      }
    }

    var temp = grid;
    grid = nextGrid;
    nextGrid = temp;

    // 若存活细胞过低，自动自补种维持生机
    if (alive < cols * 0.9) {
      seedRandom();
    }
  }

  // 赛博朋克 5 色阶调色盘 (c0: 中心高光, c1: 主球体色, c2: 边缘深度色)
  var PALETTES = [
    // 0: 主题紫色 (0s ~ 1s)
    { c0: [250, 232, 255], c1: [217, 70, 239], c2: [162, 28, 175] },
    // 1: 电光青色 (1s ~ 2s)
    { c0: [207, 250, 254], c1: [6, 182, 212],  c2: [14, 116, 144] },
    // 2: 霓虹热红 (2s ~ 3s)
    { c0: [255, 228, 230], c1: [244, 63, 94],  c2: [190, 18, 60] },
    // 3: 电光科技蓝 (3s ~ 4s)
    { c0: [219, 234, 254], c1: [59, 130, 246], c2: [29, 78, 216] },
    // 4: 极境纯白 (4s ~ 5s)
    { c0: [255, 255, 255], c1: [241, 245, 249], c2: [203, 213, 225] }
  ];

  function interpolateColor(rgbA, rgbB, t) {
    var r = Math.round(rgbA[0] + (rgbB[0] - rgbA[0]) * t);
    var g = Math.round(rgbA[1] + (rgbB[1] - rgbA[1]) * t);
    var b = Math.round(rgbA[2] + (rgbB[2] - rgbA[2]) * t);
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }

  /**
   * 计算当前时间点的球体光感颜色渐变色标
   * 0s ~ 1s: 主题紫色 (Purple)
   * 1s ~ 2s: 电光青色 (Cyan)
   * 2s ~ 3s: 霓虹热红 (Neon Red)
   * 3s ~ 4s: 科技电蓝 (Electric Blue)
   * 4s ~ 5s: 极境纯白 (Pure White，持续1s)
   * 5s 以后: 保持纯白演化
   */
  function getColorStops(now) {
    if (now >= freezeUntil) {
      return {
        c0: '#ffffff',
        c1: '#f1f5f9',
        c2: '#cbd5e1'
      };
    }

    var elapsed = Math.max(0, now - freezeStartTime);
    var sec = Math.floor(elapsed / 1000); // 0, 1, 2, 3, 4
    if (sec >= 4) {
      return {
        c0: '#ffffff',
        c1: '#f1f5f9',
        c2: '#cbd5e1'
      };
    }

    var stageTime = elapsed % 1000;
    var fromP = PALETTES[sec];
    var toP = PALETTES[sec + 1];

    // 后 160ms 内平滑过渡到下一个色彩，其余 840ms 保持 100% 饱和高光状态
    var transitionDuration = 160;
    var t = 0;
    if (stageTime > (1000 - transitionDuration)) {
      t = (stageTime - (1000 - transitionDuration)) / transitionDuration;
      t = t * t * (3 - 2 * t); // smoothstep
    }

    return {
      c0: interpolateColor(fromP.c0, toP.c0, t),
      c1: interpolateColor(fromP.c1, toP.c1, t),
      c2: interpolateColor(fromP.c2, toP.c2, t)
    };
  }

  // 同一组颜色的渐变圆点只生成一次，所有元胞共用。
  function updateDotSprite(stops, colorKey) {
    if (dotColorKey === colorKey && dotDpr === dpr) return;
    if (dotDpr !== dpr) {
      dotCanvas.width = Math.ceil(cellSize * dpr);
      dotCanvas.height = dotCanvas.width;
      dotCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
      dotSize = dotCanvas.width / dpr;
      dotDpr = dpr;
    }
    var center = dotSize / 2;
    var radius = cellSize * 0.32;
    dotCtx.clearRect(0, 0, dotSize, dotSize);
    var gradient = dotCtx.createRadialGradient(center - radius * 0.3, center - radius * 0.3, radius * 0.08, center, center, radius);
    gradient.addColorStop(0, stops.c0);
    gradient.addColorStop(0.65, stops.c1);
    gradient.addColorStop(1, stops.c2);
    dotCtx.fillStyle = gradient;
    dotCtx.beginPath();
    dotCtx.arc(center, center, radius, 0, Math.PI * 2);
    dotCtx.fill();
    dotColorKey = colorKey;
  }

  function render(stops, colorKey) {
    updateDotSprite(stops, colorKey);
    ctx.fillStyle = '#0b0e14';
    ctx.fillRect(0, 0, width, height);
    var halfDot = dotSize / 2;
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        if (grid[r * cols + c] === 1) {
          var px = c * cellSize + cellSize * 0.5;
          var py = r * cellSize + cellSize * 0.5;

          ctx.drawImage(dotCanvas, px - halfDot, py - halfDot, dotSize, dotSize);
        }
      }
    }
  }

  function loop(now) {
    animId = null;
    if (!isRunning) return;
    var stops = getColorStops(now);
    var colorKey = stops.c0 + '|' + stops.c1 + '|' + stops.c2;

    if (now < freezeUntil) {
      // 静态颜色不重画；渐变和鼠标交互最多每秒绘制 30 次。
      if ((needsRender || colorKey !== lastColorKey) && now - lastRender >= renderInterval) {
        render(stops, colorKey);
        lastColorKey = colorKey;
        lastRender = now;
        needsRender = false;
      }
    } else {
      // 5 秒后：激活康威生命游戏生灭演化规则
      if (now - lastStep >= stepInterval) {
        step();
        render(stops, colorKey);
        lastStep = now;
      }
    }
    animId = requestAnimationFrame(loop);
  }

  function syncAnimation() {
    var shouldRun = isVisible && !document.hidden;
    if (shouldRun === isRunning) return;
    isRunning = shouldRun;
    if (!isRunning) {
      pausedAt = performance.now();
      if (animId !== null) cancelAnimationFrame(animId);
      animId = null;
      return;
    }
    var now = performance.now();
    if (pausedAt !== null) {
      // 暂停期间不推进开场时间线，也不补算生命游戏帧。
      var pauseDuration = now - pausedAt;
      freezeStartTime += pauseDuration;
      freezeUntil += pauseDuration;
      pausedAt = null;
    }
    lastStep = now;
    lastRender = -Infinity;
    animId = requestAnimationFrame(loop);
  }

  container.addEventListener('mousemove', function(e) {
    if (!isRunning) return;
    var rect = canvas.getBoundingClientRect();
    var mx = e.clientX - rect.left;
    var my = e.clientY - rect.top;
    var c = Math.floor(mx / cellSize);
    var r = Math.floor(my / cellSize);
    for (var dy = -2; dy <= 2; dy++) {
      for (var dx = -2; dx <= 2; dx++) {
        var gx = (c + dx + cols) % cols;
        var gy = (r + dy + rows) % rows;
        if (Math.random() < 0.55) {
          grid[gy * cols + gx] = 1;
        }
      }
    }
    needsRender = true;
  });

  window.addEventListener('resize', resize);
  document.addEventListener('visibilitychange', syncAnimation);
  resize();
  pausedAt = performance.now();
  var visibilityObserver = new IntersectionObserver(function(entries) {
    isVisible = entries[0].isIntersecting;
    syncAnimation();
  });
  visibilityObserver.observe(container);
})();
