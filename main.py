import re
import HashMap


def askTextFromConsole():
    lines = []
    line = ""
    while line != "== END ==":
        line = input()
        lines.append(line)
    return lines


def countFrequencyOfWords(lines):
    hashMap = HashMap.HashMap()
    for line in lines:
        line = re.sub('[^a-zA-Z]', " ", line).lower()
        words = line.split(" ")
        for word in words:
            if word != "":
                frequency = hashMap.get(word)
                if frequency is not None:
                    hashMap.set(word, frequency + 1)
                else:
                    hashMap.set(word, 1)
    return hashMap

# def getWordsFromFile(path):
#     hashMap = HashMap.HashMap()
#     lines = None
#     with open(path, "r") as f:
#         lines = f.readlines()
#     for line in lines:
#         line = re.sub('[^a-zA-Z]', " ", line).lower()
#         words = line.split(" ")
#         for word in words:
#             if word != "":
#                 frequency = hashMap.get(word)
#                 if frequency is not None:
#                     hashMap.set(word, frequency + 1)
#                 else:
#                     hashMap.set(word, 1)
#     return hashMap
#
#


def askWords():
    words = []
    while True:
        inp = input()
        if inp:
            words.append(inp)
        else:
            break
    return words


if __name__ == '__main__':
    lines = askTextFromConsole()
    # hashMap = getWordsFromFile("text2.txt")
    # print("Unique words: ", hashMap.size())
    words = askWords()
    hashMap = countFrequencyOfWords(lines)
    for w in words:
        print(w, ":", hashMap.get(w))