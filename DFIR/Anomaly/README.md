# Anomaly

### Difficulty : `Medium`

### Description
I found something unusual in the network data. Can you take a closer look and find out what’s hidden within it?

### Short Writeup
Export flag.zip from the given PCAP file, which contains flag.png. After fixing the image, the flag can be revealed

25 50 4E 47 00 0A 0A 0A -> 89 50 4E 47 0D 0A 1A 0A
69 48 64 52 (iHdR) -> 49 48 44 52 (IHDR)
69 64 41 74 (idAt) -> 49 44 41 54 (IDAT)
49 4E 45 44 (INED) -> 49 45 4E 44 (IEND)

### Flag
`bi0s{sh4d0ws_r3v34l_th3_myst3ry}`

### Author

**```__m1m1__```**