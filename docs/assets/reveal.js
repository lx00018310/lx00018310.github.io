// IntersectionObserver：元素进入视口 40% 时加 .is-in，只触发一次
(function() {
  if (typeof window === 'undefined') return;

  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveals = document.querySelectorAll('.reveal');

  if (prefersReducedMotion || !('IntersectionObserver' in window)) {
    reveals.forEach(function(el) {
      el.classList.add('is-in');
    });
    return;
  }

  var io = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) {
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.25, rootMargin: '0px 0px -40px 0px' });

  reveals.forEach(function(el) {
    io.observe(el);
  });
})();
