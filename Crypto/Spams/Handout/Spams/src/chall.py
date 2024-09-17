from Crypto.Util.number import *
import os 

message = # redacted

num_msg = bytes_to_long(message.encode())

e=3
arr=[]

for i in range(e):
    N=getPrime(1024)*getPrime(1024)
    ct=pow(num_msg,e,N)
    arr.append((ct,e,N))


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "output.txt")

with open(file_path,"w+") as f:
    for i in arr:
        f.writelines([f"Ciphertext: {i[0]}\n",f"e: {i[1]}\n",f"N: {i[2]}\n\n"])


