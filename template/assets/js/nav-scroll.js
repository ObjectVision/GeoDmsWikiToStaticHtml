/* Puts the page tree back at the top.
 *
 * just-the-docs scrolls the tree on load to the current page. Up to 0.7.0 it measured the
 * link against the top of the viewport rather than against the top of the tree, so anything
 * above the tree (our masthead) was counted as scroll that had to be undone; since 0.10 it
 * centres the link with scrollIntoView. Either way the first entries of the tree disappear
 * before you have touched anything, even when the current page would have been in sight.
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
