def repeating_xor(s, k):
    if len(k) > len(s):
        k = k[:len(s)]
    else:
        k = k * (len(s) // len(k)) + k[:len(s) % len(k)]

    plaintext = bytes(ord(i) ^ ord(j) for i, j in zip(s, k))
    return plaintext.hex()


ciphertext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

print(repeating_xor(ciphertext, key))
