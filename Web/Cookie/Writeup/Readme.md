## Challenge: Cookie Manipulation

Upon logging into the page, you'll notice a series of text followed by a hint suggesting an action that involves repeating a process three times, related to admins and cookies.

Proceeding to inspect the cookie jar, you'll find a cookie named "Auth" containing seemingly random data. This data is actually a base64 encoded value of "guest", subjected to an operation repeated three times.

To progress, one must alter the value from "Guest" to "Admin" and apply base64 encoding to it three times. This manipulation will reveal another page where the flag resides in the cookie jar once again.
