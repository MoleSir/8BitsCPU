import os

dir_name = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir_name, 'DeciDisTruthTab.bin'), 'wb') as file:
    for var in range(256):
        var = str(var)
        var = int(var, base=16)
        byte = var.to_bytes(2, byteorder='little')
        file.write(byte)