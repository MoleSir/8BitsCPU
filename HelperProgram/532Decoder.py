import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name, '532decoder.bin')

with open(file_name, 'wb') as file:
    for var in range(32):
        value = 1 << var
        res = value.to_bytes(4, byteorder='little')
        file.write(res)