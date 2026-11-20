class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.data = [0] * k
        self.head = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[(self.head + self.size) % self.cap] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.head + self.size - 1) % self.cap]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap