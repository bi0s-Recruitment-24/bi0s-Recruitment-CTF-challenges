# Chainer

### Challenge Description:

Shackles made with lazy materials.\
Challenge at - `nc 74.225.222.43 5000`

**Challenge File**:
+ [Primary Link](./Handout/Chainer.zip)

**MD5 Hash: 958bc59f024833a0081a58f67ff037c6**: 

### Short Writeup:

+  This is a challenge based on AES-CBC where IV and Key is the same, the attack employed is known as IV Recovery attack.
+  The server can do three things - Encrypt plaintext, Get Flag if key is found, Receive ciphertext.
+  We will take advantage of the fact that the server returns decrypted ciphertext if it encounters a UnicodeError:
```py
    try:
        decrypted.decode() 
    except UnicodeDecodeError:
        return {"error": "Invalid plaintext: " + decrypted.hex()}
```
+  We know that:
    ### $$plaintext_i = D(piphertext) \space {\oplus} \space ciphertext_{i-1}$$
+  We send two blocks of payload that are full 0's, which from the above equation we can conclude:
    ### $$plaintext_1 \space {\oplus} \space plaintext_0 = D(piphertext_1) \space {\oplus} \space D(piphertext_0) \space {\oplus} \space ciphertext_0 \space {\oplus} \space IV$$
    ### $$plaintext_1 \space {\oplus} \space plaintext_0 = D(0) \space {\oplus} \space D(0) \space {\oplus} \space 0 \space {\oplus} \space IV$$
    ### $$plaintext_1 \space {\oplus} \space plaintext_0 = IV$$
+ Hence we can recover IV and consequentially the Key by receiving the invalid plaintext, XORing both the blocks together and sending the Key back to the server and thus the flag.

### Flag:

`bi0s{l4zy_ch41n3d_c1ph3r1n6_cl34v3d}`

### Author:

**AeroSol**