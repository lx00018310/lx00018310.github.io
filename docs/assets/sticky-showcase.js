/**
 * 2、3、4 页面物理切片擦除联动引擎 (Split-Screen Clip-Path Wipe Engine)
 * 效果：鼠标下滑时下一个画板自视口底部升起，红线之上为上一个画板，红线之下实时透出下一个画板 (背景+文字+图框一体物理切片)
 */
(function() {
  'use strict';

  var stage = document.getElementById('showcase-stage');
  if (!stage) return;

  var viewport = document.getElementById('showcase-viewport');
  var layer1 = document.getElementById('showcase-layer-1');
  var layer2 = document.getElementById('showcase-layer-2');
  if (!viewport || !layer1 || !layer2) return;

  function render() {
    var rect = stage.getBoundingClientRect();
    var windowH = window.innerHeight || document.documentElement.clientHeight;

    // 1. 严格的状态机吸附：确保在舞台区间内视口牢牢钉在屏幕中
    if (rect.top > 0) {
      // 视口尚未滚入舞台，停留在舞台顶部
      viewport.style.position = 'absolute';
      viewport.style.top = '0px';
      viewport.style.bottom = 'auto';
    } else if (rect.bottom <= windowH) {
      // 舞台已滚到底部，钉在舞台末尾，随页面向上滚入第 5 屏
      viewport.style.position = 'absolute';
      viewport.style.top = 'auto';
      viewport.style.bottom = '0px';
    } else {
      // 处于舞台联动区间，固定在视口中
      viewport.style.position = 'fixed';
      viewport.style.top = '0px';
      viewport.style.bottom = 'auto';
    }

    // 2. 物理擦除切片算法 (Clip-Path Wipe)
    // 舞台内有效可滚动高度为 200vh (stage.offsetHeight - windowH)
    var scrolled = -rect.top;

    if (scrolled <= 0) {
      // 尚未开始切入第 3 屏
      layer1.style.clipPath = 'inset(100% 0 0 0)';
      layer2.style.clipPath = 'inset(100% 0 0 0)';
    } else if (scrolled < windowH) {
      // 阶段 1：Layer 0 (考亭古街) -> Layer 1 (数字月台)
      // 进度 p 随滚动由 0 增加至 1
      var p1 = scrolled / windowH;
      // 裁剪红线从屏幕底部 (100%) 升至屏幕顶部 (0%)
      var clipY1 = (1 - p1) * 100;
      layer1.style.clipPath = 'inset(' + clipY1.toFixed(3) + '% 0 0 0)';
      layer2.style.clipPath = 'inset(100% 0 0 0)';
    } else if (scrolled < 2 * windowH) {
      // 阶段 2：Layer 1 (数字月台) -> Layer 2 (EmergentInc)
      layer1.style.clipPath = 'inset(0% 0 0 0)';
      var p2 = (scrolled - windowH) / windowH;
      var clipY2 = (1 - p2) * 100;
      layer2.style.clipPath = 'inset(' + clipY2.toFixed(3) + '% 0 0 0)';
    } else {
      // 阶段 3：完全展现 Layer 2 (EmergentInc)，并准备向上滑入第 5 屏
      layer1.style.clipPath = 'inset(0% 0 0 0)';
      layer2.style.clipPath = 'inset(0% 0 0 0)';
    }
  }

  var ticking = false;
  function requestTick() {
    if (!ticking) {
      window.requestAnimationFrame(function() {
        render();
        ticking = false;
      });
      ticking = true;
    }
  }

  window.addEventListener('scroll', requestTick, { passive: true });
  window.addEventListener('resize', requestTick, { passive: true });

  // 初始首帧渲染
  render();
})();
