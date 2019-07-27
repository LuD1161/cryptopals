from base64 import b64decode
from Crypto.Cipher import AES


def main():
    key = "YELLOW SUBMARINE"
    with open('7.txt', 'r') as f:
        data = b64decode(f.read().replace("\n", ""))
    decipher = AES.new(key, AES.MODE_ECB)
    print('Plaintext : ', decipher.decrypt(data).decode("utf-8", errors="strict"))

if __name__ == "__main__":
    main()