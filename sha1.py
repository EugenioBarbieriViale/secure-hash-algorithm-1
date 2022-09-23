msg = "abc"

def to_bin(x):
    if type(x) == int:
        return format(x, "08b")
    else:
        return "".join(format(ord(i), '08b') for i in x)

def rotate_left(x, n, w):
    return ((x << n & (2 ** w - 1)) | (x >> w - n))

def f(i, b, c, d):
    if i <= 19:
        return (b and c) or ((not b) and d)

    elif i >= 20 and i <= 39:
        return b ^ c ^ d

    elif i >= 40 and i <= 59:
        return (b and c) or (b and d) or (c and d)

    elif i >= 60 and i <= 79:
        return b ^ c ^ d


def k(i):
    if i <= 19:
        return 0x5a827999 
    
    elif i >= 20 and i <= 39:
        return 0x6ed9eba1

    elif i >= 40 and i <= 59:
        return 0x8f1bbcdc

    elif i >= 60 and i <= 79:
        return 0xca62c1d6

msg_bin = to_bin(msg)

len_bin = to_bin(len(msg_bin))
padded = msg_bin + "1" + "0"*(447-len(msg_bin)) + "0"*(64-len(len_bin)) + len_bin

padded_chunks = ["".join([padded[i] for i in range(j*32,(j+1)*32)]) for j in range(16)]

for i in range(len(padded_chunks)):
    padded_chunks[i] = "0"*48 + padded_chunks[i]

m = padded_chunks
h = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]

n = 1
for j in range(n):
    words = list()
    for i in range(80):
        if i < 15:
            words.extend([int(m[(32*i) : (32*(i+1))], 2)])
        else:
            words.extend([rotate_left(words[i-3] ^ words[i-8] ^ words[i-14] ^ words[t-16], 1, 32)])
    a = h[0]
    b = h[1]
    c = h[2]
    d = h[3]
    e = h[4]

    temp = rotate_left(a, 5, 32) + f(i, b, c, d) + e + k(i)

    e = d
    d = c
    c = rotate_left(b, 30, 32)
    b = a
    a = temp
