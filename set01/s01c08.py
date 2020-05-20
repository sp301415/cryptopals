def detect_ECB(s):
    blocksize = 16
    frequency = []

    for i, ciphertext in enumerate(s):
        blocks = [ciphertext[k*blocksize:(k+1)*blocksize] for k in range(len(ciphertext)//blocksize)]
        frequency.append((i, len(blocks)-len(set(blocks))))

    return max(frequency, key=lambda x: x[1])


with open("s01c08data", "r") as f:
    s = [bytes.fromhex(i.strip()) for i in f.readlines()]

line = detect_ECB(s)[0]
print("Detected line:", s[line])
