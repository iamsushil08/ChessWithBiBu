/* =========================================================
   NOSE GAMBIT — Navbar interactions
   Handles: mobile menu toggle, user dropdown, scroll shrink
   ========================================================= */

document.addEventListener('DOMContentLoaded', function () {

    // ---- Mobile menu toggle ----
    const navToggle = document.getElementById('navToggle');
    const navPanel = document.getElementById('navPanel');

    if (navToggle && navPanel) {
        navToggle.addEventListener('click', function () {
            const isOpen = navPanel.classList.toggle('show');
            navToggle.classList.toggle('active', isOpen);
            navToggle.setAttribute('aria-expanded', isOpen);
        });

        // Close mobile menu when a link inside it is clicked
        navPanel.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navPanel.classList.remove('show');
                navToggle.classList.remove('active');
                navToggle.setAttribute('aria-expanded', false);
            });
        });
    }

    // ---- User account dropdown ----
    const dropBtn = document.getElementById('dropBtn');
    const userDropdown = document.getElementById('userDropdown');

    if (dropBtn && userDropdown) {
        dropBtn.addEventListener('click', function (event) {
            event.stopPropagation();
            const isOpen = userDropdown.classList.toggle('show');
            dropBtn.setAttribute('aria-expanded', isOpen);
        });

        document.addEventListener('click', function (event) {
            const dropdown = document.querySelector('.dropdown');
            if (dropdown && !dropdown.contains(event.target)) {
                userDropdown.classList.remove('show');
                dropBtn.setAttribute('aria-expanded', false);
            }
        });
    }

    // ---- Shrink navbar on scroll ----
    const nav = document.getElementById('navbar');
    if (nav) {
        window.addEventListener('scroll', function () {
            nav.classList.toggle('scrolled', window.scrollY > 40);
        });
    }

});