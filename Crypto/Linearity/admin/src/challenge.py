from Crypto.Util.number import bytes_to_long, getRandomNBitInteger, getPrime
import os


hidden_msg = "bi0s{m0dul4r_4p0c4lyp53_5urv1v3d}"

x = getRandomNBitInteger(16)

m = bytes_to_long(hidden_msg.encode())
e = 65537

p = getPrime(128)
q = getPrime(128)
r = getPrime(128)
s = getPrime(128)
t = getPrime(128)

N = p*q*r*s*t

pseudo = p*q*r
totient = (p-1)*(q-1)*(r-1)

phi = (p-1)*(q-1)*(r-1)*(s-1)*(t-1)
d = pow(e,-1,phi)

assert pow(e,x,phi) == pow(d,-x,phi)

ct = pow(m,e,N)

a = 5*p + 7*q - 2*r
b = 7*p + 5*q + 3*r
c = 2*p + 3*q + 5*r

leak = pow(s,totient+1,pseudo)  

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "given.txt")

with open(file_path, "w+") as f:
    f.writelines([f"ciphertext intercepted is: {hex(ct)[2:]}\n",f"Interesting values\na: {a}, b: {b}, c: {c}, leak: {leak}\n",f"The modulus: {N}"])