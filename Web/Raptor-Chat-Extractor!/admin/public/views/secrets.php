<?php
require_once $_SERVER['DOCUMENT_ROOT'] . "/public/partials/header.html";
?>
<div class="htmlElement">
  <pre>
    <code class="external" id="external-code">
    </code>
  </pre>
</div>
<script>
    async function getHint() {
    const response = await fetch("/handle", {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `hint=${encodeURIComponent('GiveHint')}`,
    });
    const hint = await response.text();
    highlight.innerHTML = await hint;
    
    document.querySelectorAll('pre code.external').forEach((block) => {
      hljs.highlightBlock(block);
    });

    highlight.className = "external";
    highlight.classList.add('language-php', 'php', 'hljs');

    html.style.opacity = 1;
    }

    getHint();
</script>
<?php
require_once $_SERVER['DOCUMENT_ROOT'] . "/public/partials/footer.html";
?>
