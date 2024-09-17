# Linearity

### Challenge Description:

All these lines....they seemingly inter-weave over each other at a specfic point...I wonder what it means in this modular arithmetic hell.

**Challenge File**:
+ [Primary Link](./Handout/Linearity.zip)

**MD5 Hash: 58e51f0126cd94331579d33a67f6adf9**: 

### Short Writeup:

+  This is a challenge based on RSA with a system of linear equations in three variables for three of its primes are Euler's theorem for the 4th prime.
+  The given system of linear equations can be solved using any method such as elimination algebraically.
+  The main goal is to derive an equation for one of the prime and then back substitute for finding the other two unknown primes
+  For the last prime, we can use Euler's theorem (generalised Fermat's little theorem) to take advantage of the fact:
    ### $$s^{\phi(psuedo)}\mod psuedo\equiv 1$$
    ### $$s^{\phi(psuedo)+1}\mod psuedo\equiv s$$
+  The last prime can be hence derived as:
    $$t = N/(p*q*r*s)$$
+  Since all the values are derived, we can perform simple RSA decrypt to obtain the flag.

### Flag:

`bi0s{m0dul4r_4p0c4lyp53_5urv1v3d}`

### Author:

**AeroSol**