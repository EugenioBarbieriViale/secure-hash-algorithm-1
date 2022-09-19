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


def pad(msg_bin):
    temp = []
    [temp.append("0") for i in range(447-len(msg_bin))]
    zeros = "".join(temp)

    temp = []
    len_in_bin = int_to_bin(len(msg_bin))
    [temp.append("0") for i in range(64-len(len_in_bin))]
    tail = "".join(temp) + len_in_bin

    return msg_bin + "1" + zeros + tail

arr_words = ["".join([pad(msg_bin)[i] for i in range(j*32,(j+1)*32)]) for j in range(16)]

def transform(m):
    for i in range(len(m)):
        m[i] = "0"*48 + m[i]

    print(m)
    arr = []
    for j in range(len(m)):
        for i in range(80):
            if i >= 16 and i <= 79:
                word_i = int(m[i-3])^int(m[i-8])^int(m[i-14])^int(m[i-16])
        arr.append(word_i)
    return arr

print(transform(arr_words))

