import random

msg = "abc"

def str_to_bin(msg):
    return bin(int.from_bytes(str(msg).encode(), "big")).replace("b","")

def int_to_bin(msg):
    msg = int(msg)
    bin = []
    while msg >= 2:
        bin.append(str(msg%2))
        msg //= 2
        print(msg, msg%2)

    return "".join(bin)

print(int_to_bin(88))

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
    len_in_bin = str_to_bin(len(msg_bin))
    [temp.append("0") for i in range(64-len(len_in_bin))]
    tail = "".join(temp) + len_in_bin

    return msg_bin + "1" + zeros + tail
