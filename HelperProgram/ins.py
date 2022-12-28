import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name, 'ins.bin')

WE_A = 2 ** 0
CS_A = 2 ** 1

WE_B = 2 ** 2
CS_B = 2 ** 3

WE_C = 2 ** 4
CS_C = 2 ** 5


ALU_ADD = 0
ALU_SUB = 2 ** 6
ALU_OUT = 2 ** 7

WE_M = 2 ** 8
CS_M = 2 ** 9

WE_PC = 2 ** 10
EN_PC = 2 ** 11
CS_PC = 2 ** 12

HLT = 2 ** 15

micro_ins = [
    CS_M | CS_A | WE_A | WE_PC | EN_PC | CS_PC,
    CS_M | CS_B | WE_B | WE_PC | EN_PC | CS_PC,
    ALU_SUB | ALU_OUT | CS_C | WE_C,
    CS_C | WE_M | CS_M,
    HLT,
]

with open(file_name, 'wb') as file:
    for value in micro_ins:
        result = value.to_bytes(2, byteorder='little')
        file.write(result)
        print('value: {}'.format(result))

print('finish compile!!!')




