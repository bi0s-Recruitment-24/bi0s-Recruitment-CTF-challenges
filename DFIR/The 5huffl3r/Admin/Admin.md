# The 5huffl3r

### Description:
    I've Stumbled upon an unusual data stream, but something’s not quite right.Can you help me fix it?

### Solution

First xor the given file the png header :

`89 50 4E 47 0D 0A 1A 0A`

On analyzing the hex we see that the adjacent bytes have been swapped.Write a code to reconstruct the original bytes to get the flag!

#### Code :
```py
with open("<dexryptedxorfile>", "rb") as f:
    d = bytearray(f.read())

with open("flag.png", "wb") as f:
    for i in range(0,len(d),2):
        try:
            d[i],d[i+1]=d[i+1],d[i]
        except:
            continue=
    f.write(d)

```
### Flag:
``` bi0s{cr4ck3d_th3_f1n4l_hurdl3_32412} ```

### Author :
`kr4z31n`