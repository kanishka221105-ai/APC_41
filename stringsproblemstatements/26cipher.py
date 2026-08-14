text = input("Enter message: ")
shift = int(input("Enter shift value: "))
encrypted = ""
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += ch
print("Encrypted Message:", encrypted)
decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += ch
print("Decrypted Message:", decrypted)