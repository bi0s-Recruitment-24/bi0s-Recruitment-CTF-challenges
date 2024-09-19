# TR3ASUR3 CH3ST

### Difficulty - Beginner

### Description
SpongeBob's trusted "Ol' Reliable" seems to have let him down—it's empty! Or is it? Maybe there's more hidden beneath the surface. Could the answer lie in examining things layer by layer? Once you find the key, you’ll need something reliable to unlock the real treasure inside.

**#Stegnography**

### Flag format
`bi0s{...}`

### Challenge File
```MD5 Hash: 38087e29a16e2b24b9b84d7d66a3ac02 ```

### Solve
Stegsolve gives the password "neddih". Using Steghide on the image with the password gives a text file then using stegsnow with the keyword "MRKRABS" we get the flag.

### Flag
```
bi0s{Ol_Reliable_Holds_More_Than_You_Think}
```

### Author
**```rudraagh```**