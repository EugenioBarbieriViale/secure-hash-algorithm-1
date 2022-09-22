from random import randint
from numpy import left_shift

class Hash:
    def __init__(self, msg):
        self.msg = msg

    def str_to_bin(self, x):
        return bin(int.from_bytes(str(x).encode(), "big")).replace("b","")

    def int_to_bin(self, x):
        bin = []
        while x >= 1:
            bin.append(str(x%2))
            x //= 2

        return "0"*(8-len(bin)) + "".join(list(reversed(bin)))


    def random_hex(self):
        chars = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        strs = []

        for i in range(5):
            str = []
            for j in range(8):
                index = randint(0,len(chars)-1)
                str.append(chars[index])
            strs.append("".join(str))

        return strs

    def transform(self):
        self.msg_bin = self.str_to_bin(self.msg)

        len_in_bin = self.int_to_bin(len(self.msg_bin))
        padded = self.msg_bin + "1" + "0"*(447-len(self.msg_bin)) + "0"*(64-len(len_in_bin)) + len_in_bin

        self.padded_chunks = ["".join([padded[i] for i in range(j*32,(j+1)*32)]) for j in range(16)]
        m = self.padded_chunks

        for i in range(len(self.padded_chunks)):
            m[i] = "0"*48 + m[i]

        arr = []
        for j in range(len(m)):
            words = []
            for i in range(80):
                if i >= 16 and i <= 79:
                    word_i = int(m[j][i-3])^int(m[j][i-8])^int(m[j][i-14])^int(m[j][i-16])
                    words.append(word_i)
            arr.append(words)
        return arr

    def final(self):
        A = self.random_hex()[0]
        B = self.random_hex()[1]
        C = self.random_hex()[2]
        D = self.random_hex()[3]
        E = self.random_hex()[4]

        for i in range(80):
            temp = str(left_shift(int(self.str_to_bin(A)), 5)) + self.str_to_bin(self.f(i, B, C, D)) + self.str_to_bin(E) + "".join(self.transform(self.padded_chunks)[i]) + self.str_to_bin(self.K(i))

            E = D
            D = C
            C = left_shift(B, [30])
            B = A
            A = temp

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
            return "5A827999"
        
        elif i >= 20 and i <= 39:
            return "6ED9EBA1"

        elif i >= 40 and i <= 59:
            return "8F1BBCDC"

        elif i >= 60 and i <= 79:
            return "CA62C1D6"

    def run(self):
        self.transform()
        self.final()


obj = Hash("abc")
print(obj.run())
