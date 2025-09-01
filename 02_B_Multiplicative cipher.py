def encrypt(plaintext, key):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            # Normalize to uppercase
            p = ord(ch.upper()) - ord('A')
            c = (p * key) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += ch
    return ciphertext

def decrypt(ciphertext, key):
    # Calculate modular inverse of key modulo 26
    key_inv = pow(key, -1, 26)
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            c = ord(ch.upper()) - ord('A')
            p = (c * key_inv) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += ch
    return plaintext

# Usage example
key = 7
msg = "HELLO"
enc = encrypt(msg, key)
dec = decrypt(enc, key)
print("Encrypted:", enc)  # OLSSV
print("Decrypted:", dec)  # HELLO
