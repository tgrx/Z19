from collections import deque

class Queue():

    def __init__(self, max_size = 10):

        self._queue = deque(maxlen=max_size)

    def enqueue(self, item):
        self._queue.appendleft(item)

    def dequeue(self):
        return self._queue.pop()

queue = Queue()
queue.enqueue('Monday')
queue.enqueue('Tuesday')
queue.enqueue('Wednesday')
queue.enqueue('Thursday')
queue.enqueue('Friday')
queue.enqueue('Saturday')
queue.enqueue('Sunday')

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())


#Code under this comment doesnt working, but i have code with a simple working, it will be added in file level 5.1
'''if __name__ == "__main__":       
    x = []
    assert dequeue(x) is None
    assert enqueue(x, 1) is None
    assert enqueue(x, 2) is None
    assert dequeue(x) == 1
    assert enqueue(x, 3) is None
    assert dequeue(x) == 2
    assert dequeue(x) == 3
    assert dequeue(x) is None
    assert x == []'''





