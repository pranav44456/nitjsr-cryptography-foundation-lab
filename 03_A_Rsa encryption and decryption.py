# RSA Encryption & Decryption with Input/Output

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception("No modular inverse")
    return x % phi

def power(base, expo, mod):
    result = 1
    base = base % mod
    while expo > 0:
        if expo % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        expo //= 2
    return result

def generate_keys():
    p = 7919
    q = 1009
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    return power(message, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return power(ciphertext, d, n)

# Example usage
if __name__ == "__main__":
    public_key, private_key = generate_keys()
    print("Public Key :", public_key)
    print("Private Key:", private_key)

    message = int(input("\nEnter a number message to encrypt: "))
    print("Original Message:", message)

    ciphertext = encrypt(message, public_key)
    print("Encrypted Message:", ciphertext)

    decrypted = decrypt(ciphertext, private_key)
    print("Decrypted Message:", decrypted)
