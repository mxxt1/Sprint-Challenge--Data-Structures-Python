class RingBuffer:
    def __init__(self, capacity):
        # fixed size
        self.capacity = capacity
        # set fixed size for storage list. size = capacity
        self.storage = [None]*capacity
        #counter
        self.current = None

    def append(self, item):
        if self.current is None:
            pass

    def get(self):
        pass