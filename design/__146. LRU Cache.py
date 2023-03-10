# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
class DoubleList:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head = DoubleList()
        self.tail = DoubleList()
        self.head.next, self.tail.prev = self.tail, self.head
        self.hmap = {}

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_node(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next, self.tail.prev = node, node

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self._remove(node)
            self._add_node(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            #update
            node = self.hmap[key]
            node.val = value
            self._remove(node)
            self._add_node(node)
        else:
            #new node
            node = DoubleList()
            node.key = key
            node.val = value
            self._add_node(node)
            self.hmap[key] = node

            self.size += 1
            if self.size > self.cap:
                to_del = self.head.next
                self._remove(to_del)
                del self.hmap[to_del.key]
                self.size -= 1
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
