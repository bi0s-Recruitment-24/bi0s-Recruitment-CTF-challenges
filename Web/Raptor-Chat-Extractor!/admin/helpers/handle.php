<?php

// What errors my code is pitch perfect!!
error_reporting(0);

// Commands
$COMMANDS = [
    '!body'   => '-s ',
    '!header' => '-I ',
    '!time'   => '-o /dev/null -s -w "%{time_total}\\n" ',
    '!home'   => 'REDIRECT',
    '!help'   => '
Raptor Chat Extractor Help:

1. !body:
  Usage: !body [URL]
  Description: Fetch the body content of a specified URL.
  Example: !body https://example.com

2. !header:
  Usage: !header [URL]
  Description: Fetch the header of a specified URL.
  Example: !header https://example.com

3. !time:
  Usage: !time [URL]
  Description: Measure the total time taken to fetch a URL.
  Example: !time https://example.com

4. !home:
  Usage: !home
  Description: Return to home

5. !help:
  Usage: !help
  Description: Display this help guide.

Additional Notes:
- Each command should be followed by the appropriate URL (if applicable).
- For the !time command, the output will display the total time taken to get the URL.
- For the !home command, no additional URL is needed as it redirects to the home location.

Usage Examples:
- !body https://example.com
- !header https://example.com
- !time https://example.com
- !home
- !help
',
];

// Blacklist
$BLACKLIST = [
    'cat', 'touch', 'echo', 'install', 'rm', 'rmdir', 'mkdir', 'nc', 'dd', 'cp', 'ssh', 'mv', 'chmod', 'chown', 'ln', 'tee',
    'less', 'more', 'nano', 'vim', 'vi', 'view', 'grep', 'find', 'awk', 'sed', 'strings',
    'scp', 'ftp', 'wget', 'curl', 'ping', 'telnet', 'ftp', 'scp', 'rsync',
    'ps', 'top', 'kill', 'pkill', 'lsof', 'whoami', 'id', 'sudo', 'su', 'passwd',
    'sh', 'bash', 'zsh', 'csh', 'fish', 'dash', 'exec', 'eval',
    'tar', 'gzip', 'gunzip', 'bzip2', 'bunzip2', 'xz', 'unzip', 'zip', 'rar',
    'php', 'python', 'perl', 'ruby', 'java', 'gcc', 'g++', 'node', 'npm',
    'stat', 'df', 'du', 'mount', 'umount', 'chroot', 'init', 'systemctl'
];


// Handle command executions
function handleCommand($message, $COMMANDS, $BLACKLIST) {
    $command = explode(" ", trim($message));
    header('Content-Type: application/json');
    foreach ($BLACKLIST as $cmd) {
        if (stripos($command[1], $cmd) !== false) {
            $response = array(
                "type" => "error",
                "data" => "const hackerFound = true;",
            );
            $jsonResponse = json_encode($response);
            echo $jsonResponse;
            die();
        }
    }
    // If no command found return error
    if (array_key_exists($command[0], $COMMANDS)) {
        $current = $COMMANDS[$command[0]];
        switch ($command[0]) {
            case '!help':
                $response = array(
                    "type" => "yaml",
                    "data" => nl2br(htmlentities($current)),
                );
                $jsonResponse = json_encode($response);
                echo $jsonResponse;
                break;

            case '!home':
                $response = array(
                    "type" => "redirect",
                    "data" => "",
                );
                $jsonResponse = json_encode($response);
                echo $jsonResponse;
                break;

            default:
                $output = shell_exec("curl -m 10 " . $current . trim($command[1]));
                if (strlen($output) === 0) {
                    $response = array(
                        "type" => "error",
                        "data" => "const error = \"Couldn't curl the given website\";",
                    );
                    $jsonResponse = json_encode($response);
                    echo $jsonResponse;
                    die();
                } else {
                    $response = array(
                        "type" => $command[0] === "!header" ? "http" : "html",
                        "data" => htmlentities($output),
                    );
                    $jsonResponse = json_encode($response);
                    echo $jsonResponse;
                    die();
                }
            }
    } else {
        $response = array(
            "type" => "error",
            "data" => "const error = \"Invalid command found in the input!\";",
        );
        $jsonResponse = json_encode($response);
        echo $jsonResponse;
        die();
    }
}

// Give hint: View this code
if (isset($_POST["message"])) {
    handleCommand($_POST["message"], $COMMANDS, $BLACKLIST);
} elseif (isset($_POST["hint"])) {
    $hint = file_get_contents(__DIR__ . '/handle.php');

    // You think it's that easy?
    $hidden_blacklist = "\$BLACKLIST = [ 
    \"...... You don't need to know .....\"
];";
    $hint = preg_replace('/\$BLACKLIST\s*=\s*\[.*?\];/s', $hidden_blacklist, $hint);

    http_response_code(200);
    echo nl2br(htmlentities($hint));
    die();
}

