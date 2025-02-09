fruits = ["apple", "banana", "orange", "grape", "strawberry", "pineapple", "mango", "watermelon", "kiwi", "pear", "tomato"
          "peach", "plum", "cherry", "lemon", "lime", "blueberry", "raspberry", "blackberry", "avocado", "pomegranate"]
plaintext = "bi0s{...}"

def encrypt(plaintext, fruits):
    ciphertext = plaintext
    for fruit in fruits:
        fruit_length = len(fruit)
        fruit_bytes = fruit.encode()
        shifted_text = ""
        for i, char in enumerate(ciphertext):
            fruit_char = fruit_bytes[i % fruit_length]
            shifted_char = chr(ord(char) ^ fruit_char)
            shifted_text += shifted_char
        ciphertext = shifted_text
    return ciphertext

encrypted_text = encrypt(plaintext, fruits)
print(encrypted_text)