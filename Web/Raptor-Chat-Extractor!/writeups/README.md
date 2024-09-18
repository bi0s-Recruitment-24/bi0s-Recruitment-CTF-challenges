# Challenge Writeup: Remote Command Execution (RCE)

## Introduction
In this challenge, participants are presented with a chat application vulnerable to remote command execution (RCE). The application allows users to execute certain commands on the server, and the objective is to exploit this vulnerability to retrieve sensitive information or execute arbitrary commands.

## Challenge Overview
The challenge involves exploiting the vulnerable chat application to execute commands on the server remotely. Participants must understand the application's functionality, identify the vulnerable endpoint, and craft payloads to execute desired commands.

## Commands
The chat application supports the following commands:
1. **!body**: Fetch the body content of a specified URL.
2. **!header**: Fetch the header of a specified URL.
3. **!time**: Measure the total time taken to fetch a URL.
4. **!home**: Return to home.
5. **!help**: Display the help guide.

## Blacklist
To prevent abuse, certain commands are blacklisted, including potentially harmful ones like `cat`, `rm`, `mkdir`, etc.

## Solution Strategy
1. Explore the chat application and understand its functionality.
2. Craft payloads to execute commands via the vulnerable endpoints, avoiding the blacklist.
3. Execute commands to gather information or achieve specific objectives.
4. Use redirection and output formatting techniques to extract sensitive data or manipulate the server environment.
5. Be cautious of potential limitations or restrictions imposed by the application or server configuration.

## Conclusion
The Remote Command Execution (RCE) challenge provides an opportunity for participants to hone their skills in identifying and exploiting vulnerabilities in web applications. Through careful analysis and experimentation, participants can learn about the risks associated with insecure user input handling and the importance of secure coding practices.

By successfully exploiting the RCE vulnerability, participants gain insights into the potential impact of such vulnerabilities on real-world systems and the importance of implementing robust security measures to mitigate such risks. Additionally, the challenge encourages participants to think critically, develop creative solutions, and enhance their understanding of web application security principles.

Overall, the RCE challenge serves as an educational and practical exercise for participants to deepen their knowledge and expertise in cybersecurity, ultimately contributing to the development of more secure and resilient web applications.

## Payload
- Since the explode function delimiter is space, we can't add a space, so we need to use `${IFS}` to represent a space.
- Additionally, we need to include a semicolon (`;`) to end the first command.
- The payload is as follows:

    - ```bash
        !body ;head${IFS}/flag.txt
      ```

---

> Flag: bi0s{my_s3nior_s41d_cur1_is_sup3r}
