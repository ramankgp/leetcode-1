# capacity == 3
# -----------------------> most recently used(put/get)
# [{},{},{}]

# put(1,1); put(2,2); put(3,3);
# [{1,1},{2,2},{3,3}]

# get(1); -> 1
# [{2,2},{3,3},{1,1}]

# put(4,4);
#  - remove [{3,3},{1,1}]
#  - put [{3,3},{1,1},{4,4}]

# put(1,5);
#  - update [{3,3},{1,5},{4,4}]
#  - move [{3,3},{4,4},{1,5}]

# 1. constant access to head and tail -> array or linked list (with two pointers)
# 2. constant move -> doubly linked list
# 3. constant access to nodes in linked list -> hashmap<key->node>

# hashmap + doubly linked list

class LRUCache(collections.OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.keys(): return -1 
        super().move_to_end(key)
        return super().__getitem__(key)

    def put(self, key: int, value: int) -> None:
        if len(self) == self.capacity and key not in self.keys():
            super().popitem(last=False)
        super().__setitem__(key, value)
        super().move_to_end(key)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)