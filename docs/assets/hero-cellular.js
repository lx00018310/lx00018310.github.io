/**
 * 首页棋盘视口专属 · 元胞自动机生灭演化 (Cellular Automata Engine)
 * 专为首屏镂空棋盘视口定制，6px 高精网格驱动
 * 特性：初始化以 Bahnschrift / DIN 工业字形采样呈现「Cellular Automaton / Conway's Game of Life / 1970」，
 * 静态定格 5 秒后启动康威生命游戏局部规则自主演化。
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

  // 静态定格 5 秒机制
  var freezeDuration = 5000;
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

    // 在 5 秒冻结期内或首次进入时，始终重置并采样文字
    if (freezeUntil === 0 || performance.now() < freezeUntil) {
      freezeUntil = performance.now() + freezeDuration;
      seedText();
    } else {
      seedRandom();
    }
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
              // 必须同时具备红色高亮与不透明度，确保只捕获绘制的白色文字
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

  function render() {
    ctx.fillStyle = '#0b0e14';
    ctx.fillRect(0, 0, width, height);

    var radius = cellSize * 0.32;
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        if (grid[r * cols + c] === 1) {
          var px = c * cellSize + cellSize * 0.5;
          var py = r * cellSize + cellSize * 0.5;

          // 白色球体立体光晕（纯白高光 -> 极浅灰白 -> 银灰边界）
          var radGrad = ctx.createRadialGradient(px - radius * 0.3, py - radius * 0.3, radius * 0.08, px, py, radius);
          radGrad.addColorStop(0, '#ffffff');
          radGrad.addColorStop(0.65, '#f1f5f9');
          radGrad.addColorStop(1, '#cbd5e1');

          ctx.fillStyle = radGrad;
          ctx.beginPath();
          ctx.arc(px, py, radius, 0, Math.PI * 2);
          ctx.fill();
        }
      }
    }
  }

  function loop(now) {
    if (now < freezeUntil) {
      // 5 秒静态冻结期：恒定渲染文字点阵，不进行演化步进
      render();
    } else {
      // 5 秒后：激活康威生命游戏生灭演化规则
      if (now - lastStep >= stepInterval) {
        step();
        render();
        lastStep = now;
      }
    }
    animId = requestAnimationFrame(loop);
  }

  container.addEventListener('mousemove', function(e) {
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
  });

  window.addEventListener('resize', resize);
  resize();
  animId = requestAnimationFrame(loop);
})();
