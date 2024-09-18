x = lambda a, b: a * b
y = lambda a, b: a + b
z = lambda a, b: a ** b

encrypted_flag = [220, 98, 236, 196, 240, 232, 108, 204, 218, 122, 250, 264, 214, 246, 250, 140, 222, 266, 258, 134, 230, 250, 148, 274, 248]


def encrypt(key):
    s = []
    if len(key) != 25:
        print("Wrong code!")
        return
    s.extend([(x(y(ord(key[i]), i), 2)) for i in range(len(key))])
    d = sum([i for i in s])

    return s, d

def main():
    print("Enter the right code to crack this safe!")
    key = input()

    try:
        encrypted_key, q = encrypt(key)
    except (TypeError, UnboundLocalError):
        return

    if encrypted_key == encrypted_flag and q == sum([i for i in encrypted_key]):
        print("Correct code!")
        return
    else:
        print("Wrong code!")
        return

if __name__ == "__main__":
    main()

