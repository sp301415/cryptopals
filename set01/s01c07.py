from Crypto.Cipher import AES
import base64


key = b"YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)

with open("s01c07data", "r") as f:
    ciphertext = base64.b64decode(f.read())


print(cipher.decrypt(ciphertext).decode('utf-8'))
