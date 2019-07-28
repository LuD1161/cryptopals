from base64 import b64decode
from Crypto.Cipher import AES


def main():
    key = "YELLOW SUBMARINE"
    with open('10.txt', 'r') as f:
        data = b64decode(f.read().replace("\n", ""))
    iv = AES.block_size*"\x00"
    decipher = AES.new(key, AES.MODE_CBC, iv)
    print('Plaintext : ', decipher.decrypt(data).decode("utf-8", errors="strict"))

if __name__ == "__main__":
    main()