#Fruit Ninja

### Challenge Description:

I LOVE Fruit Ninja, I used all my favorite fruits to encrypt this message, do you think you can find the flag?

**Challenge File**:
+ [Primary Link](./Handout/fruit_ninja.zip)

**MD5 Hash: 157f06115c3b659ea1cb82fe3b40febe**:

### Short Writeup:

+ This is a challenge from last year's recruitment CTF
+ It uses bunch of XORs to encrypt the flag
+ Due to the lack of a comma in the array, it is not properly XORed
+ The flag can be obtained easily by re-running the provided script with the ciphertext as the input

### Flag:

`bi0s{t0mat0_!s_7he_imp0st3r_h3r3}`

### Author:

**Arch-Zero**
    
