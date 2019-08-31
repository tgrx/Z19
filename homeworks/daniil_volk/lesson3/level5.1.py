class Empty(Exception):
    pass


class ArrayQueue:
    def __init__(self):

        INIT_CAP = 10
        self._data = [None] * INIT_CAP
        self._front = 0
        self._n = 0

    def __len__(self):

        return self._n

    def __str__(self):
        return str(self._data)

    def is_empty(self):

        return self._n == 0

    def dequeue(self):

        if self.is_empty():
            raise Empty("oops, empty queue")

        dafront = self._data[self._front]

        self._data[self._front] = None  # clean up
        self._front = (self._front + 1) % (len(self._data))  # update front pointer
        self._n -= 1

        # Really, we need to resize this thing to be smaller
        # when we remove stuff from it.
        # If it is too big by a quarter, chop it in half.
        if self._n < len(self._data) // 4:
            self.resize(len(self._data) // 2)

        return dafront

    def enqueue(self, e):

        if self._n == len(self._data):
            self.resize(2 * self._n)

        insert_index = (self._front + self._n) % (len(self._data))
        self._data[insert_index] = e
        self._n += 1

    def resize(self, newsize):

        old = self._data
        walk = self._front
        self._data = [None] * newsize
        for k in range(self._n):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def first(self):
        return self._data[self._first]


if __name__ == "__main__":
    print("Testing ArrayQueue.")
    a = ArrayQueue()
    for c in "ABCDEFGHIJKLMNOPQRSTUVWX":
        a.enqueue(c)
        print(a)
    for i in range(15):
        a.dequeue()
        print(a)
    for c in "9876543":
        a.enqueue(c)
        print(a)
    for i in range(8):
        a.dequeue()
        print(a)
    print("Final:")
    print(a)
