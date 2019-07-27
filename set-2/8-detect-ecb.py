
def detect_repeated_blocks(data, blocksize=16):
    if len(data)%16:
        return False
    blocks = [data[block:block+blocksize] for block in range(0, len(data), blocksize)]
    if len(set(blocks)) == len(blocks):
        return False
    return True


def detect_ecb(data):
    detected_in = []
    for line in data:
        if detect_repeated_blocks(line):
            detected_in.append(line)
    return detected_in

def main():
    with open('8.txt', 'r') as f:
        data = f.read().split("\n")
    print(detect_ecb(data))

if __name__ == "__main__":
    main()