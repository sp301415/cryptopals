import base64


freq_data = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}


def freq(s):
    score = 0
    for c in s:
        c = c.lower()
        if c in freq_data:
            score += freq_data[c]
    return score


def single_char_xor(s):
    score = 0
    key = ""

    for c in range(256):
        p = "".join(chr(c ^ i) for i in s)
        if freq(p) > score:
            score = freq(p)
            key = chr(c)
    return key


def hamming_distance(a, b):
    assert len(a) == len(b)
    xor = [i ^ j for i, j in zip(a, b)]

    distance = 0
    for c in xor:
        distance += sum(int(i) for i in bin(c)[2:] if i == '1')

    return distance


def find_keysize(ciphertext, size, testsize):
    keysize_scored = []

    for keysize in size:
        blocks = [ciphertext[i*keysize:(i+1)*keysize] for i in range(testsize)]
        avg_distance = sum(hamming_distance(blocks[i], blocks[i+1]) for i in range(testsize-1))/((testsize-1)*keysize)
        keysize_scored.append((keysize, avg_distance))

    return min(keysize_scored, key=lambda x: x[1])


def solve_repeating_xor(ciphertext, keysize):
    blocks = [ciphertext[i*keysize:(i+1)*keysize] for i in range(len(ciphertext)//keysize)]
    blocks_transposed = [bytes(b[i] for b in blocks) for i in range(keysize)]
    return "".join(single_char_xor(blocks_transposed[i]) for i in range(keysize))


def repeating_xor(s, k):
    if len(k) > len(s):
        k = k[:len(s)]
    else:
        k = k * (len(s) // len(k)) + k[:len(s) % len(k)]

    plaintext = bytes(i ^ ord(j) for i, j in zip(s, k))
    return plaintext


with open("s01c06data", "r") as f:
    s = base64.b64decode(f.read().strip())

keysize = find_keysize(s, range(2, 40), 10)[0]
key = solve_repeating_xor(s, keysize)

print("===KEY===\n"+key)
print("===PLAINTEXT==\n"+repeating_xor(s, key).decode('utf-8'))
