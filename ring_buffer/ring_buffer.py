class RingBuffer:
    def __init__(self, capacity):
        # fixed size
        self.capacity = capacity
        # set fixed size for storage list. size = capacity
        self.storage = [None]*capacity
        #counter
        self.counter = None

    def append(self, item):
        # start the buffer if it's empty
        if self.counter is None:
            # set position 0 to item
            self.storage[0] = item
            # increment counter
            self.counter = 1
        else:
            # if buffer started set next slot to item and increment counter
            self.storage[self.counter] = item
            self.counter += 1
            # if the buffer is at capacity, reset counter and start from beginning
            if self.counter == self.capacity:
                self.counter = 0
        print(self.storage)

    def get(self):
        get_array = []
        # for everything in storage, if it exists append it to the list
        for x in self.storage:
            if x is not None:
                get_array.append(x)
        return get_array