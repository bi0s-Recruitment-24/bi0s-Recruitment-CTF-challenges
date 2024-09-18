// Declare variables
const send          = document.querySelector('.msgBtn');
const btn           = document.querySelector('.send');
const inputField    = document.getElementById('input');
const logo          = document.querySelector('.logo');
const html          = document.querySelector('.htmlElement');
const highlight     = document.getElementById('external-code');
const chat          = document.getElementById('chat');
const commands      = [
    "!body",
    "!header",
    "!home",
    "!time",
    "!help",
]

// Only for /chat path
if (location.pathname === "/chat") {
    console.log('%cI have something in crawlers prevention thingy.', 'color: green; font-weight: bold; font-size: 16px;');

    inputField.addEventListener('input', () => {
        send.style.backgroundColor = inputField.value.trim() !== '' ? 'white' : '';
        inputField.style.boxShadow = inputField.value.trim() !== '' && commands.some(command => inputField.value.trim().startsWith(command)) ? '0px 2px 2px rgba(0, 255, 0, 0.45)' : 'none';
    });

    document.addEventListener('DOMContentLoaded', () => {
        window.scrollTo(0, 0);
        html.style.opacity = highlight.innerHTML.trim() === "" ? 0 : 1;
    });

    // Handle submit
    chat.addEventListener('submit', async (event) => {
        event.preventDefault();
        html.style.opacity = 0;
        btn.setAttribute('src', '/public/images/loading.svg');
        inputField.style.boxShadow = 'none';

        const response = await fetch("/handle", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `message=${encodeURIComponent(inputField.value)}`,
        });

        inputField.value = "";
        const text = await response.text();
        const json = await JSON.parse(text);

        highlight.innerHTML = json["data"];
        document.querySelectorAll('pre code.external').forEach((block) => {
            hljs.highlightBlock(block);
        });

        highlight.className = "external";

        // Add class according to the response
        switch (json["type"]) {
            case "html":
                highlight.classList.add('language-html', 'html', 'hljs');
                break;
            case "yaml":
                highlight.classList.add('language-yaml', 'yaml', 'hljs');
                break;
            case "http":    
                highlight.classList.add('language-http', 'http', 'hljs');
                break;
            case "redirect":
                location.href = "/";
                break;
            default:
                highlight.classList.add('language-javascript', 'javascript', 'hljs');
        }

        btn.setAttribute('src', '/public/images/send.svg');
        html.style.opacity = 1;
    });
}
