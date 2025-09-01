import numpy as np
from math import gcd

class HillCipher:
    def __init__(self, key_matrix):
        self.key_matrix = np.array(key_matrix)
        self.block_size = self.key_matrix.shape[0]
        if not self._is_valid_key():
            raise ValueError("Key matrix not invertible mod 26")

    def _is_valid_key(self):
        det = int(round(np.linalg.det(self.key_matrix))) % 26
        return gcd(det, 26) == 1

    def _text_to_numbers(self, text):
        return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

    def _numbers_to_text(self, numbers):
        return ''.join(chr(int(n) + ord('A')) for n in numbers)

    def _mod_inverse(self, a, m=26):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            g, y, x = extended_gcd(b % a, a)
            return g, x - (b // a) * y, y
        g, x, _ = extended_gcd(a % m, m)
        return (x % m + m) % m if g == 1 else None

    def _matrix_inverse_mod26(self):
        det = int(round(np.linalg.det(self.key_matrix))) % 26
        det_inv = self._mod_inverse(det)
        if det_inv is None:
            return None
        if self.block_size == 2:
            a, b = self.key_matrix[0]
            c, d = self.key_matrix[1]
            adj = np.array([[d, -b], [-c, a]])
            return (det_inv * adj) % 26
        # Expand for larger matrices if needed
        raise NotImplementedError("Only 2×2 key matrix supported here")

    def encrypt(self, plaintext):
        numbers = self._text_to_numbers(plaintext)
        while len(numbers) % self.block_size != 0:
            numbers.append(ord('X') - ord('A'))
        ciphertext_numbers = []
        for i in range(0, len(numbers), self.block_size):
            block = np.array(numbers[i:i + self.block_size])
            encrypted = (self.key_matrix.dot(block) % 26)
            ciphertext_numbers.extend(encrypted)
        return self._numbers_to_text(ciphertext_numbers)

    def decrypt(self, ciphertext):
        inv = self._matrix_inverse_mod26()
        if inv is None:
            raise ValueError("Key matrix not invertible")
        numbers = self._text_to_numbers(ciphertext)
        plaintext_numbers = []
        for i in range(0, len(numbers), self.block_size):
            block = np.array(numbers[i:i + self.block_size])
            decrypted = (inv.dot(block) % 26).astype(int)
            plaintext_numbers.extend(decrypted)
        return self._numbers_to_text(plaintext_numbers)

# Example usage:
key = [[3, 2], [5, 7]]
cipher = HillCipher(key)
message = "MEETME"
encrypted = cipher.encrypt(message)
print("Encrypted:", encrypted)
print("Decrypted:", cipher.decrypt(encrypted))
