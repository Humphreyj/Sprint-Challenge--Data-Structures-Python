class RingBuffer:
    def __init__(self, capacity):
        self.capacity  = capacity

        self.queue = [None] * capacity
        self.current = 0
    def increment_current(self):
        self.current = (self.current + 1) % self.capacity
    def append(self, item):
        self.queue[self.current] = item
        self.increment_current()

    def get(self):
        return [i for i in self.queue if i is not None]