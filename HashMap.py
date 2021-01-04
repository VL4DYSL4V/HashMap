import copy


class HashMap:

    def __init__(self):
        self.__entries = [None] * 5
        self.__loadFactor = 4

    class __Entry:

        def __init__(self, key, value):
            self.__prev = None
            self.__next = None
            self.__key = copy.deepcopy(key)
            self.__value = value

        def getNext(self):
            return self.__next

        def setNext(self, entry):
            self.__next = entry

        def getPrev(self):
            return self.__prev

        def setPrev(self, entry):
            self.__prev = entry

        def getKey(self):
            return self.__key

        def getValue(self):
            return self.__value

        def setValue(self, value):
            self.__value = value

        def __repr__(self):
            return "Key: " + str(self.__key) + ", value: " + str(self.__value)

    def get(self, key):
        bucketIndex = self.__computeBucketIndex(key, len(self.__entries))
        entry = self.__entries[bucketIndex]
        while entry is not None:
            if entry.getKey() is key:
                return entry.getValue()
            entry = entry.getNext()
        return None

    def set(self, key, value):
        if self.size() / len(self.__entries) >= self.__loadFactor:
            self.__normalize()
        self.__doSet(key, value, self.__entries)

    def remove(self, key):
        bucketIndex = self.__computeBucketIndex(key, len(self.__entries))
        entry = self.__entries[bucketIndex]
        while entry is not None:
            if entry.getKey() is key:
                prev = entry.getPrev()
                next = entry.getNext()
                if prev is None:
                    #it means, it is the first in bucket
                    self.__entries[bucketIndex] = next
                else:
                    prev.setNext(next)
                if next is not None:
                    next.setPrev(prev)
                return
            entry = entry.getNext()

    def size(self):
        res = 0
        for entry in self.__entries:
            curr = entry
            while curr is not None:
                res += 1
                curr = curr.getNext()
        return res

    def __doSet(self, key, value, whereTo):
        bucketIndex = self.__computeBucketIndex(key, len(whereTo))
        lastEntry = whereTo[bucketIndex]
        if lastEntry is None:
            whereTo[bucketIndex] = HashMap.__Entry(key, value)
            return
        while lastEntry.getNext() is not None:
            if lastEntry.getKey() is key:
                lastEntry.setValue(value)
                return
            lastEntry = lastEntry.getNext()
        newEntry = HashMap.__Entry(key, value)
        lastEntry.setNext(newEntry)
        newEntry.setPrev(lastEntry)

    def __computeBucketIndex(self, key, bucketAmount):
        return hash(key) % bucketAmount

    def __normalize(self):
        newEntriesHolder = [None] * (len(self.__entries) * 2)
        for entry in self.__entries:
            curr = entry
            while curr is not None:
                self.__doSet(curr.getKey(), curr.getValue(), newEntriesHolder)
                curr = curr.getNext()

        self.__entries = newEntriesHolder

    def __repr__(self):
        res = "HashMap{ "
        for entry in self.__entries:
            curr = entry
            while curr is not None:
                res += "(" + str(curr) + "), "
                curr = curr.getNext()
        res += " }"
        return res

