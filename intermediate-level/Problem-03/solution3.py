from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            
            self.cache.popitem(last=False)


lru = LRUCache(2)
lru.put(6, 30)
lru.put(6, 78)
print(lru.get(1))  
lru.put(8, 90)     
print(lru.get(2))  
print(lru.get(3))  
