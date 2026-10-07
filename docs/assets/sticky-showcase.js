/**
 * 2、3、4 页面物理切片擦除联动引擎 (Split-Screen Clip-Path Wipe Engine)
 * 效果：鼠标下滑时下一个画板自视口底部升起，红线之上为上一个画板，红线之下实时透出下一个画板 (背景+文字+图框一体物理切片)
 */
(function() {
  'use strict';

  var stage = document.getElementById('showcase-stage');
  if (!stage) return;

  var viewport = document.getElementById('showcase-viewport');
  var layer0 = document.getElementById('showcase-layer-0');
  var layer1 = document.getElementById('showcase-layer-1');
  var layer2 = document.getElementById('showcase-layer-2');
  if (!viewport || !layer0 || !layer1 || !layer2) return;

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

    // 2. 物理互斥切片算法 (Complementary Inset Wipe)
    // 两个相邻图层在红线两侧严格空间互斥，彻底消除文字重叠
    var scrolled = -rect.top;

    if (scrolled <= 0) {
      // 尚未开始切入第 3 屏：纯展示 Layer 0
      layer0.style.clipPath = 'inset(0% 0 0% 0)';
      layer1.style.clipPath = 'inset(100% 0 0 0)';
      layer2.style.clipPath = 'inset(100% 0 0 0)';
    } else if (scrolled < windowH) {
      // 阶段 1：Layer 0 (考亭古街) -> Layer 1 (数字月台)
      var p1 = scrolled / windowH;
      var clipY1 = (1 - p1) * 100;
      // 互斥双向切片：
      // Layer 0 只保留红线上方区间 (0 ~ clipY1)，裁切下方 (100 - clipY1)
      layer0.style.clipPath = 'inset(0 0 ' + (100 - clipY1).toFixed(3) + '% 0)';
      // Layer 1 只保留红线下方区间 (clipY1 ~ 100)，裁切上方 clipY1
      layer1.style.clipPath = 'inset(' + clipY1.toFixed(3) + '% 0 0 0)';
      // Layer 2 完全隐藏
      layer2.style.clipPath = 'inset(100% 0 0 0)';
    } else if (scrolled < 2 * windowH) {
      // 阶段 2：Layer 1 (数字月台) -> Layer 2 (EmergentInc)
      // Layer 0 完全隐藏
      layer0.style.clipPath = 'inset(100% 0 0 0)';
      var p2 = (scrolled - windowH) / windowH;
      var clipY2 = (1 - p2) * 100;
      // 互斥双向切片：
      // Layer 1 只保留红线上方区间 (0 ~ clipY2)，裁切下方 (100 - clipY2)
      layer1.style.clipPath = 'inset(0 0 ' + (100 - clipY2).toFixed(3) + '% 0)';
      // Layer 2 只保留红线下方区间 (clipY2 ~ 100)，裁切上方 clipY2
      layer2.style.clipPath = 'inset(' + clipY2.toFixed(3) + '% 0 0 0)';
    } else {
      // 阶段 3：完全展现 Layer 2 (EmergentInc)，并准备向上滑入第 5 屏
      layer0.style.clipPath = 'inset(100% 0 0 0)';
      layer1.style.clipPath = 'inset(100% 0 0 0)';
      layer2.style.clipPath = 'inset(0% 0 0% 0)';
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
