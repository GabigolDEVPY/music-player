  // CURSOR
  const cursor = document.getElementById('cursor');
  const ring = document.getElementById('cursorRing');
  let mx = 0, my = 0, rx = 0, ry = 0;
  document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });
  function animateCursor() {
    rx += (mx - rx) * 0.14;
    ry += (my - ry) * 0.14;
    cursor.style.transform = `translate(${mx - 6}px, ${my - 6}px)`;
    ring.style.transform = `translate(${rx - 18}px, ${ry - 18}px)`;
    requestAnimationFrame(animateCursor);
  }
  animateCursor();
  document.querySelectorAll('a, button').forEach(el => {
    el.addEventListener('mouseenter', () => ring.classList.add('hover'));
    el.addEventListener('mouseleave', () => ring.classList.remove('hover'));
  });

  // NAV SCROLL
  const nav = document.getElementById('nav');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  });

  // SCROLL REVEAL
  const reveals = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        setTimeout(() => e.target.classList.add('visible'), 80);
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach(r => io.observe(r));

  // STAGGER siblings
  document.querySelectorAll('.features-grid, .social-links, .donate-btns').forEach(parent => {
    [...parent.querySelectorAll('.reveal, .feature-card, .social-link, .donate-btn')].forEach((el, i) => {
      el.style.transitionDelay = `${i * 80}ms`;
    });
  });

  // SCREENSHOTS auto scroll
  const scr = document.querySelector('.screenshots-scroll');
  let scrollDir = 1;
  setInterval(() => {
    if (!scr) return;
    scr.scrollLeft += scrollDir * 1;
    if (scr.scrollLeft + scr.clientWidth >= scr.scrollWidth - 5) scrollDir = -1;
    if (scr.scrollLeft <= 0) scrollDir = 1;
  }, 30);
  scr && scr.addEventListener('mouseenter', () => scrollDir = 0);
  scr && scr.addEventListener('mouseleave', () => scrollDir = 1);