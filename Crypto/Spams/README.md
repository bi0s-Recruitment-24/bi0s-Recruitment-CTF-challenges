# Spams

### Challenge Description:

I hate these spam emails I keep getting about the Chinese New Year Sale, but some part seems to be encrypted. Can I do something about it?

**Challenge File**:
+ [Primary Link](./Handout/Spams.zip)

**MD5 Hash: 25776ecb92fcd03d569d6f60e702d238**: 

### Short Writeup:

+  This is a challenge based on using Chinese Remainder Theorem to solve the system of equations with a common message.
+  There are three messages with the RSA public exponent as three, these system of equations can be used to find $message^3$
+  Start by appending all the ciphertexts to one list and moduli to an another list.
+  Find the CRT (Chinese remainder theorem) of all these ciphertexts and moduli.
+  The CRT resultant can be simply cuberooted to find the original message and hence the flag.

### Flag:

`bi0s{5unz1_c00k3d_1n_h15_3r4}`

### Author:

**AeroSol**