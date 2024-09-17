from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from random import randint
import hashlib

flag = '???'
g = getPrime(512)
p = getPrime(512)
a = randint(2,p-2)
b = randint(2,p-2)

A = pow(g,a,p)
B = pow(g,b,p)

def encrypt(flag,secret):
    sha1 = hashlib.sha1()
    sha1.update(str(secret).encode('ascii'))
    key = sha1.digest()[:16]
    cipher = AES.new(key,AES.MODE_ECB)
    result = cipher.encrypt(flag)
    return result

ciphertext = (encrypt(flag,secret))
print(g,p,b,A)
print(ciphertext)






def decrypt(ciphertext,secret): # HAHA i have stolen the secrets, I just need to use this function i made to find out what alice and bob are hiding
    sha1 = hashlib.sha1()
    sha1.update(str(secret).encode('ascii'))
    key = sha1.digest()[:16]
    cipher = AES.new(key,AES.MODE_ECB)
    result = cipher.decrypt(ciphertext)
    return result
