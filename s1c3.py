from binascii import unhexlify, hexlify 

def xor(hexstr1, hexstr2):
    decstr1, decstr2 = int(hexstr1, 16), int(hexstr2, 16)
    return hex(decstr1 ^ decstr2)

def xor_cipher(hexstr):
    pass

ct = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736" 
candidate_key = bytes([1])
keystream = candidate_key*len(ct)
# print(xor_cipher(ct))
print(bytes.fromhex(ct))
print(101^101)
