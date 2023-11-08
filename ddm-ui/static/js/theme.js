// Function to toggle the visibility of the sidebar
function toggleSidebar() {
  const sidebar = document.querySelector('.sidebar');
  const sidebarToggled = sidebar.classList.contains('toggled');

  const sidebarBrand = document.querySelector('.sidebar-brand');
  const sidebarBrandIcon = document.querySelector('.sidebar-brand-icon');
  const sidebarBrandText = document.querySelector('.sidebar-brand-text');
  const menuTextElements = document.querySelectorAll('.menu-text');
  const wrapperMenu = document.querySelector('.navbar');

  if (sidebarToggled) {
    sidebar.style.transform = 'translateX(-100%)';
    sidebarBrand.style.display = 'none';
    sidebarBrandIcon.style.display = 'none';
    sidebarBrandText.style.display = 'none';
    wrapperMenu.style.display = 'none'
    menuTextElements.forEach((item) => {
      item.style.display = 'none';
    });
  } else {
    sidebar.style.transform = 'none';
    sidebarBrand.style.display = 'flex';
    sidebarBrandIcon.style.display = 'flex';
    sidebarBrandText.style.display = 'block';
    wrapperMenu.style.display = 'flex'
    menuTextElements.forEach((item) => {
      item.style.display = 'inline';
    });
  }
}

// Apply the "toggled" class to the sidebar element by default
document.addEventListener('DOMContentLoaded', function () {
  const sidebar = document.querySelector('.sidebar');
  sidebar.classList.add('toggled');

  // Call the function to toggle the sidebar and menu text
  toggleSidebar();

  // Add event listeners to the sidebar toggles to call the toggleSidebar function when clicked
  const sidebarToggles = document.querySelectorAll('#sidebarToggle, #sidebarToggleTop');
  sidebarToggles.forEach((toggle) => {
    toggle.addEventListener('click', toggleSidebar);
  });
});

// Function to toggle the visibility of the menu text
function toggleMenuText() {
  const sidebar = document.querySelector('.sidebar');
  const sidebarToggled = sidebar.classList.contains('toggled');

  const sidebarBrandText = document.querySelector('.sidebar-brand-text');
  const menuTextElements = document.querySelectorAll('.menu-text');

  sidebarBrandText.style.display = sidebarToggled ? 'none' : 'block';
  menuTextElements.forEach((item) => {
    item.style.display = sidebarToggled ? 'none' : 'inline';
  });
}

// Apply the "toggled" class to the sidebar element by default
document.addEventListener('DOMContentLoaded', function () {
  const sidebar = document.querySelector('.sidebar');
  sidebar.classList.add('toggled');

  // Call the functions to toggle the sidebar and menu text
  toggleSidebar();
  toggleMenuText();

  // Add event listeners to the sidebar toggles to call the toggle functions when clicked
  const sidebarToggles = document.querySelectorAll('#sidebarToggle, #sidebarToggleTop');
  sidebarToggles.forEach((toggle) => {
    toggle.addEventListener('click', function () {
      toggleSidebar();
      toggleMenuText();
    });
  });
});

(function() {
  "use strict";

  var sidebar = document.querySelector('.sidebar');
  var sidebarToggles = document.querySelectorAll('#sidebarToggle, #sidebarToggleTop');
  
  if (sidebar) {
    var collapseEl = sidebar.querySelector('.collapse');
    var collapseElementList = [].slice.call(document.querySelectorAll('.sidebar .collapse'));
    var sidebarCollapseList = collapseElementList.map(function (collapseEl) {
      return new bootstrap.Collapse(collapseEl, { toggle: false });
    });

    for (var toggle of sidebarToggles) {
      toggle.addEventListener('click', function(e) {
        document.body.classList.toggle('sidebar-toggled');
        sidebar.classList.toggle('toggled');

        if (sidebar.classList.contains('toggled')) {
          for (var bsCollapse of sidebarCollapseList) {
            bsCollapse.hide();
          }
        }
      });
    }

    window.addEventListener('resize', function() {
      var vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);

      if (vw < 768) {
        for (var bsCollapse of sidebarCollapseList) {
          bsCollapse.hide();
        }
      }
    });
  }

  var fixedNavigation = document.querySelector('body.fixed-nav .sidebar');

  if (fixedNavigation) {
    fixedNavigation.on('mousewheel DOMMouseScroll wheel', function(e) {
      var vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);

      if (vw > 768) {
        var e0 = e.originalEvent;
        var delta = e0.wheelDelta || -e0.detail;
        this.scrollTop += (delta < 0 ? 1 : -1) * 30;
        e.preventDefault();
      }
    });
  }

  var scrollToTop = document.querySelector('.scroll-to-top');

  if (scrollToTop) {
    window.addEventListener('scroll', function() {
      var scrollDistance = window.pageYOffset;

      if (scrollDistance > 100) {
        scrollToTop.style.display = 'block';
      } else {
        scrollToTop.style.display = 'none';
      }
    });
  }
})();
