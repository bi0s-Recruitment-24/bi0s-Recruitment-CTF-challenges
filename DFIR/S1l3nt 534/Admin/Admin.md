# S1l3nt 534

### Difficulty - **Hard**

### Description 

```
During a recent mission, a conversation between the crew was captured. However, the text seems unclear and cryptic.Can you help uncover the hidden treasure?
```

**#Steganography #Encoded**

### Flag format
`bi0s{...}`


### Solution

First we export the wav file named `ocean.wav` from the pcapng file. While going through the packets we see encoded conversation with raw data in the ICMP packets which is encoded as base64 as
```
V2XigJl2ZSBhcnJpdmVkIGF0IHRoZSBzaGlwd3JlY2suIExldOKAmXMgZ2V0IHRoZSBsb2cgd2UgbmVlZC4=
R290IGl0LCBDYXB0YWluLiBXaGF04oCZcyB0aGUgY29kZSB0byBvcGVuIHRoZSBjaGVzdD8=
VXNlIHRoaXMgY29kZSB0byBvcGVuIGl0OiBzaDNsbDVfNHRfczM0
 ```
 which on decoding gives 
 ```
We’ve arrived at the shipwreck. Let’s get the log we need.Got it, Captain. What’s the code to open the chest?Use this code to open it: sh3ll5_4t_s34
```
Now extracting the embedded png file using deepsound and the password `sh3ll5_4t_s34` and fixing

```
89 50 4E 47 0D 0A 1A 0A
49 48 44 52 (IHDR)
49 44 41 54 (IDAT)
49 45 4E 44 (IEND)
```
We get the flag as : `bi0s{h1dd3n_tr345ur3_br0u9ht_t0_l19ht}`

### Flag 
`bi0s{h1dd3n_tr345ur3_br0u9ht_t0_l19ht}`

### Author

**```__m1m1__```**