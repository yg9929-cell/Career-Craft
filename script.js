/* =========================================================
   PORTFOLIO SCRIPT
   Handles: mobile menu, active nav link, scroll animations,
   back-to-top button and the footer year.
   You normally do not need to edit this file.
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {
  const navbar    = document.getElementById("navbar");
  const navToggle = document.getElementById("navToggle");
  const navLinks  = document.getElementById("navLinks");
  const links     = navLinks.querySelectorAll("a");
  const toTop     = document.getElementById("toTop");
  const sections  = document.querySelectorAll("main section[id]");

  /* ---------- 1. Mobile menu open / close ---------- */
  navToggle.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");
    navToggle.classList.toggle("open", isOpen);
    navToggle.setAttribute("aria-expanded", isOpen);
  });

  // Close the menu after tapping a link (smooth scrolling is handled by CSS)
  links.forEach((link) => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("open");
      navToggle.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });

  /* ---------- 2. Navbar shadow + back-to-top visibility ---------- */
  function onScroll() {
    navbar.classList.toggle("scrolled", window.scrollY > 20);
    toTop.classList.toggle("show", window.scrollY > 500);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  toTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* ---------- 3. Highlight the current section in the nav ---------- */
  const navObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          links.forEach((link) => {
            link.classList.toggle(
              "active",
              link.getAttribute("href") === "#" + entry.target.id
            );
          });
        }
      });
    },
    { rootMargin: "-45% 0px -50% 0px" }
  );
  sections.forEach((section) => navObserver.observe(section));

  /* ---------- 4. Fade-in animation when scrolling ---------- */
  const revealItems = document.querySelectorAll(".reveal");

  if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );

    // Small stagger so cards in the same row appear one after another
    revealItems.forEach((item) => {
      const siblings = item.parentElement.querySelectorAll(":scope > .reveal");
      const index = Array.prototype.indexOf.call(siblings, item);
      item.style.transitionDelay = Math.min(index, 5) * 0.08 + "s";
      revealObserver.observe(item);
    });
  } else {
    // Very old browsers: just show everything
    revealItems.forEach((item) => item.classList.add("visible"));
  }

  /* ---------- 5. Footer year updates itself ---------- */
  document.getElementById("year").textContent = new Date().getFullYear();
});
