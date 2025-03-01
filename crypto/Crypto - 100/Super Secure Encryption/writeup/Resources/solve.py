import binascii
from pwn import xor

with open("msg.txt") as h:
    encrypted_message = binascii.unhexlify(h.readline().strip())
    encrypted_flag = binascii.unhexlify(h.readline().strip())

test = b'This is just a test message and can totally be ignored.'

xor_1 = xor(encrypted_message,encrypted_flag)
xor_2 = xor(xor_1,test)

flag = xor_2[:len(encrypted_flag)]

print(f"{flag=}")