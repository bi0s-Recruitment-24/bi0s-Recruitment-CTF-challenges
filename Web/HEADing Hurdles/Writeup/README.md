# **Challenge:** HEADing Hurdles 


The first hint suggests that this is a header-based challenge (as the name includes HEAD). If we set the user-agent to secbrowser, we will progress to the next level.

The next step says `people referring to me as ghostbyte`, indicating the referer... setting the referer to ghostbyte advances us to the next level.

Next, the challenge asks for the localhost IP... setting x-forwarded-for to 127.0.0.1 moves us to the next level.

Continuing, we receive a message: `Gr8! Now the breached data can only be seen by POSTman.` This hints at using a POST request. Sending a POST request to the URL with these headers completes the challenge and reveals the flag.

Flag: `bi0s{heard_of_headers?}`