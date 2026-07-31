/* Puts the page tree back at the top.
 *
 * just-the-docs scrolls the tree on load so the current page sits three rows down. It
 * measures the link against the top of the viewport rather than against the top of the tree,
 * so anything above the tree (our masthead) is counted as scroll that has to be undone, and
 * the first entries disappear before you have touched anything.
 *
 * This runs on load, after the theme's own handler, and scrolls only when the current page
 * would otherwise be out of sight.
 */
window.addEventListener("load", function () {
  var nav = document.getElementById("site-nav");
  if (!nav) return;

  nav.scrollTop = 0;

  var link = nav.querySelector(".nav-list-link.active");
  if (!link) return;

  var navBox = nav.getBoundingClientRect();
  var box = link.getBoundingClientRect();
  if (box.bottom > navBox.bottom || box.top < navBox.top) {
    nav.scrollTop += box.top - navBox.top - 2 * box.height;
  }
});
