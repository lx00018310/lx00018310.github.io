/**
 * 首页棋盘视口专属 · 元胞自动机生灭演化 (Cellular Automata Engine)
 * 专为首屏镂空棋盘视口定制，纯原生 Canvas 驱动
 */
(function() {
  'use strict';

  var canvas = document.getElementById('hero-cellular-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  if (!ctx) return;

  var container = canvas.parentElement;
  var width = 0, height = 0, dpr = 1;
  var cellSize = 16;
  var cols = 0, rows = 0;
  var grid = null, nextGrid = null;
  var lastStep = 0;
  var stepInterval = 180; // 180ms 步进
  var animId = null;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = container.clientWidth || 1200;
    height = container.clientHeight || 1000;

    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    cols = Math.ceil(width / cellSize);
    rows = Math.ceil(height / cellSize);

    grid = new Uint8Array(cols * rows);
    nextGrid = new Uint8Array(cols * rows);

    seedRandom();
  }

  function seedRandom() {
    grid.fill(0);
    // 随机播种多个活动核心（根据超大画幅网格成比例增加）
    var clusterCount = Math.max(8, Math.floor((cols * rows) / 220));
    for (var i = 0; i < clusterCount; i++) {
      var cx = Math.floor(Math.random() * cols);
      var cy = Math.floor(Math.random() * rows);
      var radius = 4;
      for (var dy = -radius; dy <= radius; dy++) {
        for (var dx = -radius; dx <= radius; dx++) {
          if (dx * dx + dy * dy <= radius * radius && Math.random() < 0.48) {
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

    // 若存活细胞过低，自动重新播种
    if (alive < cols * 0.8) {
      seedRandom();
    }
  }

  function render() {
    ctx.fillStyle = '#0b0e14';
    ctx.fillRect(0, 0, width, height);

    // 绘制暗色微网格
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (var x = 0; x <= width; x += cellSize) {
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
    }
    for (var y = 0; y <= height; y += cellSize) {
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
    }
    ctx.stroke();

    // 绘制存活元胞（以紫色球体/渐变粒子体现）
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        if (grid[r * cols + c] === 1) {
          var px = c * cellSize + cellSize * 0.5;
          var py = r * cellSize + cellSize * 0.5;
          var radius = cellSize * 0.38;

          // 白色球体立体光晕（纯白高光 -> 极浅白灰 -> 银灰边界）
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
    if (now - lastStep >= stepInterval) {
      step();
      render();
      lastStep = now;
    }
    animId = requestAnimationFrame(loop);
  }

  container.addEventListener('mousemove', function(e) {
    var rect = canvas.getBoundingClientRect();
    var mx = e.clientX - rect.left;
    var my = e.clientY - rect.top;
    var c = Math.floor(mx / cellSize);
    var r = Math.floor(my / cellSize);
    for (var dy = -1; dy <= 1; dy++) {
      for (var dx = -1; dx <= 1; dx++) {
        var gx = (c + dx + cols) % cols;
        var gy = (r + dy + rows) % rows;
        if (Math.random() < 0.6) {
          grid[gy * cols + gx] = 1;
        }
      }
    }
  });

  window.addEventListener('resize', resize);
  resize();
  animId = requestAnimationFrame(loop);
})();
