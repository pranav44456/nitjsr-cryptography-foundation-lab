# Simple DES in Python (educational only)

# pip install pycryptodome if you want real DES

# S-box and permutation tables are included directly

IP = [58,50,42,34,26,18,10,2,
      60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6,
      64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,
      59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5,
      63,55,47,39,31,23,15,7]

FP = [40,8,48,16,56,24,64,32,
      39,7,47,15,55,23,63,31,
      38,6,46,14,54,22,62,30,
      37,5,45,13,53,21,61,29,
      36,4,44,12,52,20,60,28,
      35,3,43,11,51,19,59,27,
      34,2,42,10,50,18,58,26,
      33,1,41,9,49,17,57,25]

E = [32,1,2,3,4,5,4,5,6,7,8,9,
     8,9,10,11,12,13,12,13,14,15,16,17,
     16,17,18,19,20,21,20,21,22,23,24,25,
     24,25,26,27,28,29,28,29,30,31,32,1]

P = [16,7,20,21,29,12,28,17,
     1,15,23,26,5,18,31,10,
     2,8,24,14,32,27,3,9,
     19,13,30,6,22,11,4,25]

SBOX = [
# S1
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
 0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
 4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
 15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
# S2
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
 3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
 0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
 13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
# ... (you’d need all 8 S-boxes, omitted here for brevity)
]

def string_to_bitlist(s):
    result = []
    for c in s:
        val = ord(c)
        for i in range(7, -1, -1):
            result.append((val >> i) & 1)
    return result

def bitlist_to_string(b):
    result = ''
    for i in range(0, len(b), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | b[i+j]
        result += chr(byte)
    return result

def permute(block, table):
    return [block[x-1] for x in table]

def xor(t1, t2):
    return [x ^ y for x,y in zip(t1,t2)]

def feistel(r, k):
    # expand
    r = permute(r, E)
    r = xor(r, k)
    # S-box (simplified, only S1 for demo!)
    s_out = []
    b = r[:6]
    row = (b[0]<<1) + b[5]
    col = (b[1]<<3) + (b[2]<<2) + (b[3]<<1) + b[4]
    val = SBOX[0][16*row+col]
    s_out += [(val>>3)&1,(val>>2)&1,(val>>1)&1,val&1]
    return permute(s_out, P[:4])  # simplified

def des_encrypt_block(block, key):
    block = permute(block, IP)
    l, r = block[:32], block[32:]
    for i in range(1):  # just 1 round for demo
        l, r = r, xor(l, feistel(r, key[:48]))
    block = permute(r+l, FP)
    return block

# Example
plain = "ABCDEFGH"   # 8 chars = 64 bits
key   = "12345678"
plain_bits = string_to_bitlist(plain)
key_bits   = string_to_bitlist(key)

cipher_bits = des_encrypt_block(plain_bits, key_bits)
cipher_text = bitlist_to_string(cipher_bits)

print("Plain:", plain)
print("Cipher:", cipher_text.encode())
