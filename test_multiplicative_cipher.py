
def multiplicative_decrypt(text, key):
   
    for i in range(26):
        if (key * i) % 26 == 1:
            inv = i
            break
    else:
        return "No inverse exists for this key."
    
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr(((ord(char) - shift) * inv) % 26 + shift)
        else:
            result += char
    return result
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - shift - key) % 26 + shift)
        else:
            plaintext += char
    return plaintext


ciphertext = "UWEEWGNMGUZBYXY"
print(f"Ciphertext: {ciphertext}\n")

for key in range(26):
    plain = multiplicative_decrypt(ciphertext, key)
    print(f"Key {key:2} -> {plain}")
    #// MISSIONCOMPLETE
