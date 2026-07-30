// MathJax 3 configuration. MathJax reads this global object at load time, so this
// script must run before the mathjax bundle itself (both are deferred and therefore
// execute in document order; see _includes/mathjax.html).
MathJax = {
  tex: {
    // The wikis write inline math as $...$, which MathJax 3 does NOT recognise by
    // default (it only does \(...\)). Without this every inline formula shows up as
    // raw LaTeX. Code and pre blocks are skipped by MathJax, so $ in code examples
    // is not affected; \$ stays a literal dollar because of processEscapes.
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true
  },
  options: {
    renderActions: {
      // Also render <script type="math/tex"> nodes, which kramdown emits for math.
      // Copied from https://docs.mathjax.org/en/latest/upgrading/v2.html#changes-in-the-mathjax-api
      findScript: [10, function (doc) {
        for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
          const display = !!node.type.match(/; *mode=display/);
          const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display);
          const text = document.createTextNode('');
          node.parentNode.replaceChild(text, node);
          math.start = {node: text, delim: '', n: 0};
          math.end = {node: text, delim: '', n: 0};
          doc.math.push(math);
        }
      }, '']
    }
  }
};
