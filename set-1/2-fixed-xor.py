from base64 import b64encode

def decodeHex(givenString):
    return bytes.fromhex(givenString)

givenInput = "1c0111001f010100061a024b53535009181c"
xorInput = "686974207468652062756c6c277320657965"

def xorFixed(input1, input2):
    output = b""
    for i,j in zip(input1, input2):
        output += bytes([i^j])
    return output

def main():
    print(xorFixed(decodeHex(givenInput), decodeHex(xorInput)).hex())

if __name__ == "__main__":
    main()