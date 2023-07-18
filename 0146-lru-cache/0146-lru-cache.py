class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.n = capacity
        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        self.store[key] = self.store.pop(key)

        return self.store[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)
        else:
            if self.n:
                self.n -= 1
            else:
                self.store.pop(next(iter(self.store)))

        self.store[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)