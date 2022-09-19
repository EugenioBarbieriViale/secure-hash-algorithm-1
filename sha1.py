import random

msg = "abc"

def str_to_bin(x):
    return bin(int.from_bytes(str(x).encode(), "big")).replace("b","")

def int_to_bin(x):
    bin = []
    while x >= 1:
        bin.append(str(x%2))
        x //= 2

    return "0"*(8-len(bin)) + "".join(list(reversed(bin)))

msg_bin = str_to_bin(msg)

def random_hex():
    chars = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    strs = []

    for i in range(5):
        str = []
        for j in range(8):
            index = random.randint(0,len(chars)-1)
            str.append(chars[index])
        strs.append("".join(str))

    return strs

len_in_bin = int_to_bin(len(msg_bin))
padded = msg_bin + "1" + "0"*(447-len(msg_bin)) + "0"*(64-len(len_in_bin)) + len_in_bin

arr_words = ["".join([padded[i] for i in range(j*32,(j+1)*32)]) for j in range(16)]

def transform(m):
    for i in range(len(m)):
        m[i] = "0"*48 + m[i]

    arr = []
    for j in range(len(m)):
        words = []
        for i in range(80):
            if i >= 16 and i <= 79:
                word_i = int(m[j][i-3])^int(m[j][i-8])^int(m[j][i-14])^int(m[j][i-16])
                words.append(word_i)
        print(words)
        arr.append(words)
    return arr

# print(transform(arr_words))
# transform(arr_words)
