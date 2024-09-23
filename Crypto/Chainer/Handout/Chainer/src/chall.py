from Crypto.Cipher import AES
import os
import sys


KEY = os.urandom(16)
FLAG = # redacted

def hex_try(s):
    try:
        s = bytes.fromhex(s)
    except ValueError as e:
        print({"error": e})
        sys.exit()
    return s
    
def encrypt(plaintext):
    plaintext = hex_try(plaintext)
    if len(plaintext) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}

    cipher = AES.new(KEY, AES.MODE_CBC, KEY)
    encrypted = cipher.encrypt(plaintext)

    return {"ciphertext": encrypted.hex()}

def get_flag(key):
    key = hex_try(key)

    if key == KEY:
        return ({"plaintext": FLAG.encode().hex()},1)
    else:
        return ({"error": "invalid key"},0)


def receive(ciphertext):
    ciphertext = hex_try(ciphertext)
    if len(ciphertext) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}

    cipher = AES.new(KEY, AES.MODE_CBC, KEY)
    decrypted = cipher.decrypt(ciphertext)

    try:
        decrypted.decode() 
    except UnicodeDecodeError:
        return {"error": "Invalid plaintext: " + decrypted.hex()}

    return {"success": "Your message has been received"}


def main():
    s='''+-----------------------------------------------------------------------+
    |Welcome to this interactive encryption menu! What would you like to do?|
    |                                                                       |
    | (1) Encrypt plaintext                                                 |
    | (2) Get Flag                                                          |
    | (3) Receive Ciphertext                                                |
    | (4) Exit                                                              |
    +-----------------------------------------------------------------------+'''
    print(s)
    while True:

        response = input("Your response: ")
        if response == '1':
            plaintext = input("Plaintext (hex): ")
            print(encrypt(plaintext))
        elif response == '2':
            print("Bro thought it would be that easy")
            key = input("Key (hex): ")
            flag, num = get_flag(key)
            if num:
                print(f"ggs!\n{flag}")
            else:
                print("Sorry lil bro")
            break
        elif response == '3':
            ciphertext = input("Ciphertext (hex): ")
            print(receive(ciphertext))
        else:
            print("Bye")
            break

main()
        

        