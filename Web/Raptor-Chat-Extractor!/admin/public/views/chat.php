<?php
require_once $_SERVER['DOCUMENT_ROOT'] . "/public/partials/header.html";
?>

<div class="htmlElement">
  <pre>
    <code class="external" id="external-code">
    </code>
  </pre>
</div>

<div class="msgBar">
  <form id="chat" action="/chat" method="post">
      <input id="input" type="text" name="message" placeholder="Enter your message..." autocomplete="off">
      <button class="msgBtn" type="submit"><img class="send" src="/public/images/send.svg" alt="Send"></button>
  </form>
<div class="fade"></div>
</div>

<?php
require_once $_SERVER['DOCUMENT_ROOT'] . "/public/partials/footer.html";
?>
