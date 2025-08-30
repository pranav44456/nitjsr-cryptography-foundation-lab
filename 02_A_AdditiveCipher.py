def encrypt_additive(plaintext, key):
    result = ""
    for char in plaintext.upper():
        if char.isalpha():  # Only shift alphabets
            # Convert A=0,...,Z=25
            shifted = (ord(char) - ord('A') + key) % 26
            result += chr(shifted + ord('A'))
        else:
            result += char  # Keep spaces/punctuation
    return result


def decrypt_additive(ciphertext, key):
    result = ""
    for char in ciphertext.upper():
        if char.isalpha():
            shifted = (ord(char) - ord('A') - key) % 26
            result += chr(shifted + ord('A'))
        else:
            result += char
    return result


# Example usage
plaintext = "HELLO WORLD"
key = 3

encrypted = encrypt_additive(plaintext, key)
decrypted = decrypt_additive(encrypted, key)

print(f"Plaintext : {plaintext}")
print(f"Key       : {key}")
print(f"Encrypted : {encrypted}")
print(f"Decrypted : {decrypted}")
