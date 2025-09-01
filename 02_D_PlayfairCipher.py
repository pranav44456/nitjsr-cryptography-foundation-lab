def create_playfair_matrix(key):
    # Remove duplicates, uppercase, and preserve order
    key = ''.join(sorted(set(key), key=key.index)).upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # typically omit J
    matrix = []

    for char in key:
        if char in alphabet:
            matrix.append(char)
            alphabet = alphabet.replace(char, "")

    matrix += list(alphabet)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return -1, -1

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.replace('J', 'I').upper()
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

# Example usage:
plaintext = "HELLO"
key = "KEYWORD"
ciphertext = playfair_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
