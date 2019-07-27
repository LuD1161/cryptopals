from base64 import b64encode
import string

def decodeHex(givenString):
    return bytes.fromhex(givenString)


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


givenString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
lenGivString = len(givenString)
scores = []
for char in string.printable: # should use range(256) instead of string.printable
    xorredOutput = xorFixed((char*lenGivString).encode("utf-8", errors="strict"), decodeHex(givenString))
    score = calculateScore(xorredOutput)
    scores.append(score)

maxScore = max(scores)
possibleKeys = [index for index, value in enumerate(scores) if value == maxScore]
for key in possibleKeys:
    print("Key {0} - {1}".format(string.printable[key], xorFixed((string.printable[key]*lenGivString).encode("utf-8", errors="strict"), decodeHex(givenString))))