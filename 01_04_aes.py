from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(s):
    # PKCS7 padding
    pad_len = 16 - (len(s) % 16)
    return s + bytes([pad_len] * pad_len)

def unpad(s):
    return s[:-s[-1]]

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def aes_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext))
    return plaintext

if __name__ == "__main__":
    key = get_random_bytes(16)  # AES-128 key
    plaintext = b"HelloSymmetric!"

    print("Original:", plaintext)

    ciphertext = aes_encrypt(key, plaintext)
    print("Encrypted (hex):", ciphertext.hex())

    decrypted = aes_decrypt(key, ciphertext)
    print("Decrypted:", decrypted)
