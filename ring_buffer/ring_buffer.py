class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    ci = self.current
    if ci == len(self.storage) - 1:
        self.storage[ci] = item
        self.current = 0
    else:
        self.storage[ci] = item
        self.current += 1

  def get(self):
    return [item for item in self.storage if item is not None]
    # for i in self.storage:
    #     if i is None:
    #         pass
    #     else:
    #         get_storage.append(i)
    # return get_storage
  