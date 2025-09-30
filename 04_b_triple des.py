from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Create a Triple DES key (16 or 24 bytes)
key = DES3.adjust_key_parity(get_random_bytes(24))

# Create cipher object
cipher = DES3.new(key, DES3.MODE_CBC)

# Data to encrypt
data = b"Secret message here"
padded_data = pad(data, DES3.block_size)

# Encrypt
ciphertext = cipher.encrypt(padded_data)
iv = cipher.iv

print(f"Ciphertext: {ciphertext.hex()}")

# Decrypt
decipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
decrypted_padded = decipher.decrypt(ciphertext)
decrypted = unpad(decrypted_padded, DES3.block_size)

print(f"Decrypted: {decrypted.decode()}")
