from base64 import b64decode
import string


def findHammingDistance(s1, s2):
    bs1 = bin(int.from_bytes(s1, 'big'))
    bs2 = bin(int.from_bytes(s2, 'big'))
    distance = 0
    for i,j in zip(bs1, bs2):
        if i != j:
            distance += 1
    return distance


def findMin(keySizes):
    minNum = min(keySizes)
    minNums = []
    for num in keySizes:
        if num == minNum:
            minNums.append(num)
    return minNums


def findKeySize(data):
    results = []
    for keySize in range(2, 41):
        chunks = [data[i:i+keySize] for i in range(0, len(data), keySize)]
        distance = 0
        for i in range(len(chunks) - 1):
            distance += (findHammingDistance(chunks[i], chunks[i+1])/keySize)   # Normalize through dividing by keySize
        results.append({'key': keySize, 'distance':(distance/(len(chunks)-1))})
    keySizes = []
    results = sorted(results, key=lambda x:x['distance'])
    # for i in range(len(results)):
    #     print("Guess {0} - Hamming Distance {1}".format(results[i]['key'], results[i]['distance']))
    return results


def generateBlocks(data, key):
    blocks = []
    for i in range(key):
        blocks.append(data[0+i::key])
    return blocks


def xorFixed(input1, input2):
    output = b""
    for i,j in zip(input1, input2):
        output += bytes([i^j])
    return output


englishLetterFreq = {' ': 13.0, 'E' : 12.0,'T' : 9.10,'A' : 8.12,'O' : 7.68,'I' : 7.31,'N' : 6.95,'S' : 6.28,'R' : 6.02,'H' : 5.92,'D' : 4.32,'L' : 3.98,'U' : 2.88,'C' : 2.71,'M' : 2.61,'F' : 2.30,'Y' : 2.11,'W' : 2.09,'G' : 2.03,'P' : 1.82,'B' : 1.49,'V' : 1.11,'K' : 0.69,'X' : 0.17,'Q' : 0.11,'J' : 0.10,'Z' : 0.07 }

def calculateScore(input1):
    score = 0
    for letter in input1.upper():
        score += englishLetterFreq.get(chr(letter), 0)
    return score


def findSingleCharKey(givenString):
    lenGivString = len(givenString)
    scores = []
    for char in range(256):
        xorredOutput = xorFixed((chr(char)*lenGivString).encode("utf-8", errors="strict"), givenString)
        score = calculateScore(xorredOutput)
        scores.append(score)

    maxScore = max(scores)
    for index, value in enumerate(scores):
        if value == maxScore:
            return index    
    # possibleKeys = [index for index, value in enumerate(scores) if value == maxScore]
    # for key in possibleKeys:
        # print("Key {0} - {1}".format(chr(key), xorFixed((chr(key)*lenGivString).encode("utf-8", errors="strict"), givenString)))
    # return possibleKeys

def repeatingXor(input, key):
    output = b""
    lenInput = len(input)
    lenKey = len(key)
    for i in range(lenInput):
        output += bytes([input[i]^key[i%lenKey]])
    # return output.decode("utf-8", errors="strict")
    return output

def main():
    with open('6.txt', 'r') as f:
        data = f.read().replace("\n","")
    data = b64decode(data)
    keysizes = findKeySize(data)
    final_keys = []
    for keysize in keysizes[:4]:
        blocks = generateBlocks(data, keysize['key'])
        keys = []
        for block in blocks:
            keys.append(findSingleCharKey(block))
        keys = "".join(chr(key) for key in keys)
        final_keys.append(keys)
    # for key in final_keys[3:]:
    for key in final_keys:
        print("Key : {0} \nMessage : {1}\n\n\n".format(key, repeatingXor(data, key.encode("utf-8", errors="strict"))))

if __name__ == "__main__":
    main()