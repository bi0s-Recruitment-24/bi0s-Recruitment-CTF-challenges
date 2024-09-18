<?php

$REQUEST = $_SERVER['REQUEST_URI'];
$PATH    = __DIR__ . '/public';

// Handle requests
switch ($REQUEST) {
    case '/':
        require_once $PATH . '/views/main.php';
        break;

    case '/robots.txt':
        require_once __DIR__ . '/robots.txt';
        break;

    case '/s3cr37':
        require_once $PATH . '/views/secrets.php';
        break;

    case '/chat':
        require_once $PATH . '/views/chat.php';
        break;

    case '/handle':
        require_once __DIR__ . '/helpers/handle.php';
        break;
        
    default:
        require_once $PATH . '/views/404.php';
        break;
}
