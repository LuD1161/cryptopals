
def pkcs_padding(data, blocksize=16):
    amountOfPadding = (blocksize - len(data)%blocksize)%blocksize
    return data + bytes([amountOfPadding])*amountOfPadding


def main():
    data = input("Enter data to be padded : ")
    blocksize = int(input("Enter blocksize : "))
    data = data.encode("utf-8", errors="strict")
    print(pkcs_padding(data, blocksize))

if __name__ == "__main__":
    main()