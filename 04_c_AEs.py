from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# AES key (16, 24, or 32 bytes for AES-128, AES-192, AES-256)
key = get_random_bytes(32)  # AES-256

# Initialization Vector
iv = get_random_bytes(16)

# Create cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# Data to encrypt
data = b"This is a secret message"
padded_data = pad(data, AES.block_size)

# Encrypt the data
ciphertext = cipher.encrypt(padded_data)

print(f"Ciphertext (hex): {ciphertext.hex()}")

# Decrypt
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
decrypte
