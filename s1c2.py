def xor(hexstr1, hexstr2):
    decstr1, decstr2 = int(hexstr1, 16), int(hexstr2, 16)
    return hex(decstr1 ^ decstr2)

print(xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))