# -*- coding: utf-8 -*-
import binascii
from ast import literal_eval


# input= "ÿ°Î"
input= "5ÿô‘ 7s YN ¥╔            ╚š╔?þˆÀ"
hex = binascii.hexlify(input)
binary = bin(int(binascii.hexlify(input), 16))
# print binary
print hex
float_str = "0x00"+str(hex[4:10])
result = float(literal_eval(float_str))
output = int(binary, 2)

print float_str
print result