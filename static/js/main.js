// ─── PRELOADER FIX ───────────────────────────────────────────
// This MUST be at the very top before everything else!
window.addEventListener('load', function () {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        setTimeout(function () {
            preloader.classList.add('hidden');
        }, 800);
    }
});


// ─── WAIT FOR PAGE TO LOAD ────────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {


    // ─── 1. NAVBAR SCROLL EFFECT ─────────────────────────────
    const navbar = document.querySelector('.navbar');

    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }


    // ─── 2. HAMBURGER MENU ───────────────────────────────────
    const hamburger = document.getElementById('hamburger');
    const navLinks  = document.getElementById('nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function () {
            navLinks.classList.toggle('open');
            hamburger.classList.toggle('active');
        });

        document.querySelectorAll('.nav-links a').forEach(function (link) {
            link.addEventListener('click', function () {
                navLinks.classList.remove('open');
                hamburger.classList.remove('active');
            });
        });
    }


    // ─── 3. ACTIVE NAV LINK ON SCROLL ────────────────────────
    const sections = document.querySelectorAll(
        '#home, #about, #skills, #projects, #experience, #education, #contact'
    );
    const navItems = document.querySelectorAll('.nav-links a');

    window.addEventListener('scroll', function () {
        let current = '';

        sections.forEach(function (section) {
            const sectionTop    = section.offsetTop - 120;
            const sectionHeight = section.clientHeight;

            if (window.scrollY >= sectionTop &&
                window.scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        navItems.forEach(function (link) {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    });


    // ─── 4. FADE IN ANIMATIONS ───────────────────────────────
    const fadeElements = document.querySelectorAll('.fade-in');

    if (fadeElements.length > 0) {
        const fadeObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    fadeObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold : 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        fadeElements.forEach(function (el) {
            fadeObserver.observe(el);
        });
    }


    // ─── 5. SKILL BAR ANIMATIONS ─────────────────────────────
    const skillBars = document.querySelectorAll('.skill-progress');

    if (skillBars.length > 0) {
        const skillObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    const width = entry.target.getAttribute('data-width');
                    entry.target.style.width = width + '%';
                    skillObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.3
        });

        skillBars.forEach(function (bar) {
            skillObserver.observe(bar);
        });
    }


    // ─── 6. SCROLL TO TOP BUTTON ─────────────────────────────
    const scrollTopBtn = document.getElementById('scrollTop');

    if (scrollTopBtn) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 300) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        });

        scrollTopBtn.addEventListener('click', function () {
            window.scrollTo({
                top     : 0,
                behavior: 'smooth'
            });
        });
    }


    // ─── 7. SMOOTH SCROLL FOR NAV LINKS ──────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top     : offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });


    // ─── 8. HAMBURGER ANIMATION ──────────────────────────────
    const hamburgerStyle = document.createElement('style');
    hamburgerStyle.textContent = `
        .hamburger.active span:nth-child(1) {
            transform: rotate(45deg) translate(5px, 5px);
        }
        .hamburger.active span:nth-child(2) {
            opacity  : 0;
            transform: translateX(-10px);
        }
        .hamburger.active span:nth-child(3) {
            transform: rotate(-45deg) translate(5px, -5px);
        }
    `;
    document.head.appendChild(hamburgerStyle);


    // ─── 9. TYPING EFFECT FOR HERO ───────────────────────────
    const tagline = document.querySelector('.text-gray');

    if (tagline) {
        const text          = tagline.textContent.trim();
        tagline.textContent = '';
        let index           = 0;

        function typeWriter() {
            if (index < text.length) {
                tagline.textContent += text.charAt(index);
                index++;
                setTimeout(typeWriter, 60);
            }
        }

        setTimeout(typeWriter, 1000);
    }


    // ─── 10. PROJECT CARDS HOVER 3D EFFECT ───────────────────
    document.querySelectorAll('.project-card').forEach(function (card) {
        card.addEventListener('mousemove', function (e) {
            const rect    = card.getBoundingClientRect();
            const x       = e.clientX - rect.left;
            const y       = e.clientY - rect.top;
            const centerX = rect.width  / 2;
            const centerY = rect.height / 2;
            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;

            card.style.transform =
                `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
            card.style.transition = 'transform 0.1s ease';
        });

        card.addEventListener('mouseleave', function () {
            card.style.transform  = '';
            card.style.transition = 'transform 0.3s ease';
        });
    });


    // ─── 11. COUNTER ANIMATION ───────────────────────────────
    function animateCounter(element, target, duration) {
        let start  = 0;
        const step = target / (duration / 16);

        const timer = setInterval(function () {
            start += step;
            if (start >= target) {
                element.textContent = target + '+';
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(start) + '+';
            }
        }, 16);
    }

    document.querySelectorAll('.counter').forEach(function (counter) {
        const counterObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    const target = parseInt(
                        counter.getAttribute('data-target')
                    );
                    animateCounter(counter, target, 2000);
                    counterObserver.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });

        counterObserver.observe(counter);
    });


    // ─── 12. FORM INPUT ANIMATIONS ───────────────────────────
    document.querySelectorAll('.form-input').forEach(function (input) {
        input.addEventListener('focus', function () {
            this.parentElement.classList.add('focused');
        });

        input.addEventListener('blur', function () {
            this.parentElement.classList.remove('focused');
        });
    });


    // ─── 13. SOCIAL PILLS ENTRANCE ANIMATION ─────────────────
    const pills = document.querySelectorAll('.social-pill');
    pills.forEach(function (pill, index) {
        pill.style.opacity   = '0';
        pill.style.transform = 'translateY(20px)';

        setTimeout(function () {
            pill.style.transition = 'all 0.5s ease';
            pill.style.opacity    = '1';
            pill.style.transform  = pill.classList.contains('tilt-pill')
                ? 'rotate(-10deg) translateY(-10px)'
                : 'translateY(0)';
        }, 500 + (index * 150));
    });


    // ─── 14. MARQUEE PAUSE ON HOVER ──────────────────────────
    const marquee = document.querySelector('.marquee-content');
    if (marquee) {
        marquee.addEventListener('mouseenter', function () {
            this.style.animationPlayState = 'paused';
        });
        marquee.addEventListener('mouseleave', function () {
            this.style.animationPlayState = 'running';
        });
    }


    // ─── 15. NAVBAR FIXED ON SCROLL ──────────────────────────
    const navbarScrollStyle = document.createElement('style');
    navbarScrollStyle.textContent = `
        .navbar.scrolled {
            position  : fixed;
            top       : 12px;
            left      : 50%;
            transform : translateX(-50%);
            width     : 90%;
            max-width : 1100px;
            z-index   : 1000;
            animation : navSlideDown 0.3s ease;
        }

        @keyframes navSlideDown {
            from {
                opacity  : 0;
                transform: translateX(-50%) translateY(-20px);
            }
            to {
                opacity  : 1;
                transform: translateX(-50%) translateY(0);
            }
        }
    `;
    document.head.appendChild(navbarScrollStyle);


    // ─── 16. CONTACT FORM SUBMIT ANIMATION ───────────────────
    const contactForm = document.getElementById('contactForm');
    const submitBtn   = document.getElementById('submitBtn');

    if (contactForm && submitBtn) {
        contactForm.addEventListener('submit', function () {
            submitBtn.style.opacity        = '0.7';
            submitBtn.style.width          = '100%';
            submitBtn.style.justifyContent = 'center';
            submitBtn.innerHTML            = `
                Sending...
                <span class="yellow-square-arrow">
                    <i class="fas fa-spinner fa-spin"></i>
                </span>
            `;
        });
    }


    // ─── 17. AUTO HIDE ALERT MESSAGES ────────────────────────
    const alertMessages = document.querySelectorAll('.alert-message');
    alertMessages.forEach(function (msg) {
        setTimeout(function () {
            msg.style.transition = 'all 0.5s ease';
            msg.style.opacity    = '0';
            msg.style.transform  = 'translateY(-10px)';
            setTimeout(function () {
                msg.remove();
            }, 500);
        }, 5000);
    });


    // ─── 18. ABOUT CARDS STAGGER ANIMATION ───────────────────
    const aboutCards = document.querySelectorAll('.about-inner-card');
    aboutCards.forEach(function (card, index) {
        card.style.opacity   = '0';
        card.style.transform = 'translateY(30px)';

        const cardObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    setTimeout(function () {
                        card.style.transition = 'all 0.6s ease';
                        card.style.opacity    = '1';
                        card.style.transform  = 'translateY(0)';
                    }, index * 200);
                    cardObserver.unobserve(card);
                }
            });
        }, { threshold: 0.2 });

        cardObserver.observe(card);
    });


    // ─── 19. STEP CARDS STAGGER ANIMATION ────────────────────
    const steps = document.querySelectorAll('.step');
    steps.forEach(function (step, index) {
        step.style.opacity   = '0';
        step.style.transform = 'translateY(30px)';

        const stepObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    setTimeout(function () {
                        step.style.transition = 'all 0.6s ease';
                        step.style.opacity    = '1';
                        step.style.transform  = 'translateY(0)';
                    }, index * 200);
                    stepObserver.unobserve(step);
                }
            });
        }, { threshold: 0.2 });

        stepObserver.observe(step);
    });


    // ─── 20. PAGE TITLE ANIMATION ────────────────────────────
    const originalTitle = document.title;

    document.addEventListener('visibilitychange', function () {
        if (document.hidden) {
            document.title = '👋 Come Back! | ' + originalTitle;
        } else {
            document.title = originalTitle;
        }
    });


    // ─── 21. ACTIVE HOME LINK ON LOAD ────────────────────────
    const homeLink = document.querySelector('.nav-links a[href="#home"]');
    if (homeLink) {
        homeLink.classList.add('active');
    }


}); // ─── END OF DOMContentLoaded ─────────────────────────────