def hash_func(key):
    return ord(key[0]) % 10

class HashTable:
    def __init__(self):
        self.table = [None] * 10

    def set(self, key, value):
        self.table[hash_func(key)] = value

    def get(self, key):
        return self.table[hash_func(key)]

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class ChainedHashTable(HashTable):
    def set(self, key, value):
        index_key = ord(key[0])
        hash_address = hash_func(key)
        if self.table[hash_address] == None:
            self.table[hash_address] = [[index_key, value]]
        else:
            self.table[hash_address].append([index_key, value])

# Test code

ht = ChainedHashTable()
ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)

print(ht.get('hello'), end=' ') 
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()

ht.set('hello2', 5)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')