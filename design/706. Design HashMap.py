# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

class MyHashMap:
    def __init__(self):
        self.size = 300
        self.buff = [[] for _ in range(self.size)]        

    def put(self, key: int, value: int) -> None:
        index = key%self.size          
        for i, (k,v) in enumerate(self.buff[index]):   #update value
            if k==key:
                self.buff[index][i] = (key, value)
                break
        else:                                           #new value
            self.buff[index].append((key,value))

    def get(self, key: int) -> int:
        index = key%self.size   
        for i, (k,v) in enumerate(self.buff[index]):   
            if k==key:
                return self.buff[index][i][1]               
        else:                       
            return -1       

    def remove(self, key: int) -> None:
        index = key%self.size   
        for k,v in self.buff[index]:   
            if k==key:
                self.buff[index].remove((k,v))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)