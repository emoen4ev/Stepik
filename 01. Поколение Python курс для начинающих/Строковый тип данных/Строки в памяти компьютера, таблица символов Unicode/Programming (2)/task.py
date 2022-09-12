key = int(input())
cryptogram = input()

for c in cryptogram:
    new_code = ord(c) - key
    if new_code >= ord("a"):
        print(chr(new_code), end="")
    elif new_code < ord("a"):
        new_key = (ord("a") - 1) - new_code
        print(chr(ord("z") - new_key), end="")
