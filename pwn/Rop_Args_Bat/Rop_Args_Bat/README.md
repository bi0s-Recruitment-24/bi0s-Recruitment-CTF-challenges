# Rop_Args_Bat

### Challenge Description

Batman needs to find Robin and B4tMite can help. Help him figure out the spell to summon Robin.

**Challenge File**:
+ [Primary Link](https://drive.google.com/file/d/1WYYdSfjtx78WHHAtbRnVGXv9dgK8LP7y/view?usp=sharing)

**MD5 Hash**: e4ed14d5fbada9d90bcfc461fee0c9a5

### Short Writeup:

+ Call the `call_robin` function with arguments `0xdeadbeef` and `0xcafebabe` to read out the flag.
+ Main function has buffer overflow and no canary so ROP is possible.
+ Binary is statically-linked to provide more gadgets.
+ Just create a rop-chain that puts `0xdeadbeef` in RDI and `0xcafebabe` in RSI to win.

### Flag:

bi0s{7h3_B0Y_W0nd3r}

### Author:

**B4tMite**
