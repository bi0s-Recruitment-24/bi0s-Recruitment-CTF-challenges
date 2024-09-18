# Hidden Secrets

### Difficulty : `Beginner`

### Description
Hey, young ninja! A secret is hidden deep within this image. Can you uncover the secret?


### Short Writeup

Using Binwalk, we can extract flag.zip from chall.jpg by the command: `binwalk -e chall.jpg`

After extracting flag.jpg, fix the file by changing the header: 00 00 -> FF D8. 
This will reveal the flag


### Flag
`bi0s{3ff0rtl355_v1ct0ry_010}`

### Author

**```__m1m1__```**