from base64 import b64encode

def hextobase64(hexstr: str):
    return b64encode(bytes.fromhex(hexstr))

print(hextobase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))