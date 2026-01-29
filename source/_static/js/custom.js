/* ============================================
 * ADT / ADT42 — custom.js (Sphinx + Furo)
 * Objetivo:
 *  - Respetar WCAG 2.1 AA
 *  - No romper header móvil (burger / TOC)
 *  - Consumir variables CSS del theme
 * ============================================ */

(function () {
  "use strict";

  /* =========================================================
   * Utilidades
   * ========================================================= */

  function cssVar(name, fallback = "") {
    const value = getComputedStyle(document.documentElement)
      .getPropertyValue(name)
      .trim();
    return value || fallback;
  }

  function onReady(fn) {
    if (document.readyState !== "loading") {
      fn();
    } else {
      document.addEventListener("DOMContentLoaded", fn);
    }
  }

  /* =========================================================
   * 1) Barra de progreso de lectura (segura en mobile)
   * ========================================================= */

  function initReadingProgress() {
    const bar = document.createElement("div");
    bar.id = "reading-progress-bar";

    bar.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      width: 0%;
      background: ${cssVar("--color-brand-primary", "#104E5E")};
      z-index: 50;
      transition: width 0.15s ease;
    `;

    document.body.appendChild(bar);

    function update() {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight =
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;

      if (docHeight <= 0) return;

      const percent = (scrollTop / docHeight) * 100;
      bar.style.width = `${Math.min(100, Math.max(0, percent))}%`;
    }

    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  /* =========================================================
   * 2) Botón Back-to-Top (WCAG friendly)
   * ========================================================= */

  function initBackToTop() {
    const btn = document.createElement("button");
    btn.id = "back-to-top";
    btn.type = "button";
    btn.setAttribute("aria-label", "Volver arriba");

    btn.textContent = "↑";

    btn.style.cssText = `
      position: fixed;
      right: 1rem;
      bottom: 1rem;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      border: none;
      cursor: pointer;
      display: none;
      background: ${cssVar("--color-brand-primary", "#104E5E")};
      color: ${cssVar("--color-background-primary", "#F2F6F8")};
      z-index: 60;
      font-size: 1.2rem;
    `;

    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    window.addEventListener("scroll", function () {
      btn.style.display = window.scrollY > 300 ? "block" : "none";
    });

    document.body.appendChild(btn);
  }

  /* =========================================================
   * 3) Enlaces externos (icono accesible)
   * ========================================================= */

  function markExternalLinks() {
    const links = document.querySelectorAll(
      ".content a[href^='http']:not([href*='" + location.host + "'])"
    );

    links.forEach(function (link) {
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener noreferrer");
      link.setAttribute(
        "aria-label",
        (link.textContent || "Enlace externo") + " (abre en nueva pestaña)"
      );
    });
  }

  /* =========================================================
   * 4) Abreviaturas (tooltip sin romper contraste)
   * ========================================================= */

  function enhanceAbbr() {
    const abbrs = document.querySelectorAll("abbr[title]");

    abbrs.forEach(function (abbr) {
      abbr.style.cursor = "help";
      abbr.style.textDecoration = "none";
      abbr.style.borderBottom = "1px dotted currentColor";
    });
  }

  /* =========================================================
   * 5) Copy-button feedback (sin colores hardcodeados)
   * ========================================================= */

  function enhanceCopyButtons() {
    document.addEventListener("click", function (ev) {
      const btn = ev.target.closest(".copybtn");
      if (!btn) return;

      btn.classList.add("adt-copy-success");
      setTimeout(() => btn.classList.remove("adt-copy-success"), 900);
    });
  }

  /* =========================================================
   * 6) Resaltado al navegar por hash (#)
   * ========================================================= */

  function highlightHashTarget() {
    if (!location.hash) return;

    const id = location.hash.slice(1);
    const el = document.getElementById(id);
    if (!el) return;

    el.classList.add("adt-highlighted");
    setTimeout(() => el.classList.remove("adt-highlighted"), 2000);
  }

  /* =========================================================
   * Inicialización
   * ========================================================= */

  onReady(function () {
    initReadingProgress();
    initBackToTop();
    markExternalLinks();
    enhanceAbbr();
    enhanceCopyButtons();
    highlightHashTarget();
  });
})();

/* ============================================================
   Sidebar Search — Enhancements (WCAG/UX)
   Para template: sidebar/search.html  (input#sidebar-search-input)
   ============================================================ */

(function () {
  "use strict";

  function onReady(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  onReady(function () {
    const input = document.getElementById("sidebar-search-input");
    if (!input) return;

    // 1) Atajo "/" para enfocar (cuando no estás escribiendo en un input/textarea)
    document.addEventListener("keydown", function (ev) {
      if (ev.defaultPrevented) return;

      const key = ev.key;
      const target = ev.target;

      const isTypingContext =
        target &&
        (target.tagName === "INPUT" ||
          target.tagName === "TEXTAREA" ||
          target.isContentEditable);

      // "/" enfoca búsqueda (sin interferir si ya estás escribiendo)
      if (!isTypingContext && key === "/") {
        ev.preventDefault();
        input.focus();
        // Selecciona texto si ya hay algo (útil para reemplazar rápido)
        if (input.value) input.select();
      }

      // 2) Esc limpia búsqueda si está enfocada
      if (key === "Escape" && document.activeElement === input) {
        input.value = "";
        input.blur();
      }
    });

    // 3) Evita que el navegador autocompletar “rompa” UX si no lo quieres
    // (ya pones autocomplete="off" en HTML, esto es extra defensivo)
    input.setAttribute("autocomplete", "off");
    input.setAttribute("autocapitalize", "off");
    input.setAttribute("autocorrect", "off");

    // 4) UX: al enfocar, si hay contenido, seleccionar para reemplazar rápido
    input.addEventListener("focus", function () {
      if (input.value) input.select();
    });
  });
})();

/* ============================================================
   Sidebar Scroll Wrappers — Enhancements
   Para templates: sidebar/scroll-start.html / sidebar/scroll-end.html
   Objetivo:
   - Evitar scroll del body cuando el sidebar overlay está abierto (mobile)
   - No interferir con Furo ni con accesibilidad
   ============================================================ */

(function () {
  "use strict";

  function onReady(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  onReady(function () {
    const navToggle = document.getElementById("__navigation");
    if (!navToggle) return;

    let lastScrollY = 0;

    function lockBodyScroll() {
      // Guardar posición
      lastScrollY = window.scrollY || document.documentElement.scrollTop || 0;

      // Bloquear scroll del body sin “brincos”
      document.body.style.position = "fixed";
      document.body.style.top = `-${lastScrollY}px`;
      document.body.style.left = "0";
      document.body.style.right = "0";
      document.body.style.width = "100%";
    }

    function unlockBodyScroll() {
      // Restaurar scroll
      const top = document.body.style.top;
      document.body.style.position = "";
      document.body.style.top = "";
      document.body.style.left = "";
      document.body.style.right = "";
      document.body.style.width = "";

      // Volver a la posición previa
      const y = top ? Math.abs(parseInt(top, 10)) : lastScrollY;
      window.scrollTo(0, y);
    }

    function apply() {
      // Solo bloquear en pantallas pequeñas (overlay)
      const isMobile = window.matchMedia("(max-width: 768px)").matches;
      const isOpen = !!navToggle.checked;

      if (isMobile && isOpen) lockBodyScroll();
      else unlockBodyScroll();
    }

    // Cambio al abrir/cerrar
    navToggle.addEventListener("change", apply);

    // Si rota o cambia tamaño
    window.addEventListener("resize", function () {
      // Si ya está bloqueado y deja de ser mobile, liberar
      apply();
    });

    // Estado inicial
    apply();
  });
})();

