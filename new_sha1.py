from random import randint
from numpy import left_shift

class Hash:
    def __init__(self, msg):
        self.msg = msg

    def to_bin(self, x):
        if type(x) == int:
            return format(x, "08b")
        else:
            return "".join(format(ord(i), '08b') for i in x)

    def rotate_left(self, x, n, w):
        return ((x << n & (2 ** w - 1)) | (x >> w - n))

    def transform(self):
        self.msg_bin = self.to_bin(self.msg)

        len_bin = self.to_bin(len(self.msg_bin))
        padded = self.msg_bin + "1" + "0"*(447-len(self.msg_bin)) + "0"*(64-len(len_bin)) + len_bin

        self.padded_chunks = ["".join([padded[i] for i in range(j*32,(j+1)*32)]) for j in range(16)]

        for i in range(len(self.padded_chunks)):
            self.padded_chunks[i] = "0"*48 + self.padded_chunks[i]

        m = self.padded_chunks
        h = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]
        print(m)

        words = list()
        for i in range(80):
            if i < 15:
                words.extend([int(m[(32*i) : (32*(i+1))], 2)])
            else:
                words.extend([rotate_left(words[i-3] ^ words[i-8] ^ words[i-14] ^ words[t-16], 1, 32)])

        return words

    # def final(self):
    #     A = h[0]
    #     B = h[1]
    #     C = h[2]
    #     D = h[3]
    #     E = h[4]

    #     for i in range(80):

    #         temp = (A << 5) + self.f(i, B, C, D) + E + self.padded_chunks[i] + K(i)

    #         E = D
    #         D = C
    #         C = str(left_shift(int(self.to_bin(B)), 30))
    #         B = A
    #         A = temp

    #         print(temp)

    def f(self, i, B, C, D):
        if i <= 19:
            return (B and C) or ((not B) and D)

        elif i >= 20 and i <= 39:
            return B ^ C ^ D

        elif i >= 40 and i <= 59:
            return (B and C) or (B and D) or (C and D)

        elif i >= 60 and i <= 79:
            return B ^ C ^ D

     def K(self, i):
        if i <= 19:
            return 0x5a827999 
        
        elif i >= 20 and i <= 39:
            return 0x6ed9eba1

        elif i >= 40 and i <= 59:
            return 0x8f1bbcdc

        elif i >= 60 and i <= 79:
            return 0xca62c1d6

    def run(self):
        self.transform()
        # self.final()


obj = Hash("abc")
obj.run()
