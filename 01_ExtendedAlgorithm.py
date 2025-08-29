def compute_gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = compute_gcd_extended(b, a % b)
    x = y1 - (a // b) * x1
    y = x1
    return gcd, x, y

a, b = 35, 15
gcd, x, y = compute_gcd_extended(a, b)
print(f"gcd({a}, {b}) = {gcd}, x = {x}, y = {y}")
