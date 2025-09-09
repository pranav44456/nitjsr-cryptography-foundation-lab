# Polynomial arithmetic under GF(2^p)

# Convert integer to polynomial representation (binary string)
def poly_to_str(p):
    return bin(p)[2:]

# Addition in GF(2^p) = XOR
def poly_add(a, b):
    return a ^ b

# Multiplication in GF(2^p) without modulo reduction
def poly_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result

# Multiplication with modulo reduction using irreducible polynomial
def poly_mul_mod(a, b, mod_poly):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        # reduce if degree exceeds mod_poly
        if a & (1 << (mod_poly.bit_length() - 1)):
            a ^= mod_poly
        b >>= 1
    return result

# Example usage
if __name__ == "__main__":
    # Example polynomials: x^3 + x + 1 = 0b1011 (11), x^2 + 1 = 0b101 (5)
    a = 0b1011   # 11
    b = 0b101    # 5
    mod_poly = 0b10011  # x^4 + x + 1 (irreducible for GF(2^4))

    print("a =", poly_to_str(a))
    print("b =", poly_to_str(b))
    print("Addition (a+b) =", poly_to_str(poly_add(a, b)))
    print("Multiplication (a*b) =", poly_to_str(poly_mul(a, b)))
    print("Multiplication modulo =", poly_to_str(poly_mul_mod(a, b, mod_poly)))
