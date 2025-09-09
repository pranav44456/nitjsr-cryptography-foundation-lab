
def decrypt_additive(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - shift - key) % 26 + shift)
        else:
            plaintext += char
    return plaintext


ciphertext = "MKTGLFBMHKWXKLGHP"
print(f"Ciphertext: {ciphertext}\n")

for key in range(26):
    plain = decrypt_additive(ciphertext, key)
    print(f"Key {key:2} -> {plain}")
    #TRANSMITORDERSNOW
