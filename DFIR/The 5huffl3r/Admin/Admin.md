# The 5huffl3r

### Difficulty -  **Hard**

### Description:
The image you’re after isn’t as it seems.The first bytes hold a secret that echoes through the entire file. With a bit of careful work, you can put the pieces back in place. Can you reveal what’s hidden?

**#Scripting #Filestructure**

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

**```kr4z31n```**
