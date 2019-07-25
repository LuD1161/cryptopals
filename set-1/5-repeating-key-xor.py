from base64 import b64encode
import string


def repeatingXor(input, key):
    output = b""
    lenInput = len(input)
    lenKey = len(key)
    for i in range(lenInput):
        output += bytes([input[i]^key[i%lenKey]])
    return output


def main():
    givenString = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    key = "ICE".encode("utf-8", errors="strict")
    givenString = givenString.encode("utf-8", errors="strict")
    print(repeatingXor(givenString, key).hex())

if __name__ == "__main__":
    main()