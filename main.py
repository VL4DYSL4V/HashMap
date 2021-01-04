import copy
import re
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import HashMap


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hashMap = HashMap.HashMap()
    # hashMap.set("and", 1)
    # print(hashMap)
    # hashMap.set(copy.deepcopy("and"), 2)
    # print(hashMap)
    # hashMap.set("and", 3)
    # print(hashMap)
    lines = None
    d = {}
    with open("text2.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        words = line.split(" ")
        for word in words:
            word = re.sub('[^a-zA-Z]', '', word).lower()
            frequencyD = d.get(word)
            if frequencyD is not None:
                d[word] = frequencyD + 1
            else:
                d[word] = 1

            frequency = hashMap.get(word)
            if frequency is not None:
                hashMap.set(word, frequency + 1)
            else:
                hashMap.set(word, 1)
print(len(d))
print(d)

print(hashMap)
print(hashMap.size())
print(hashMap.get("and"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
