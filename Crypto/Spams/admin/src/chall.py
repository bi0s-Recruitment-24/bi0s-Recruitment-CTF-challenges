from Crypto.Util.number import *
import os 

message = "CHINESE NEW YEAR ALERT!! SOMETHING MAO ZEDONG WANTED TO TELL YOU: bi0s{5unz1_c00k3d_1n_h15_3r4}"

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


