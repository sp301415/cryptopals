
def xor(a, b):
    return bytes(i^j for i, j in zip(a, b))


s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"

print(xor(bytes.fromhex(s1), bytes.fromhex(s2)).decode('utf-8'))
