"""
We use array to store the number of unique hash. In each array index we store the node which is a complex object to hold
the key, value, and a pointer to the next node. By next node we mean that if two keys collide and share the same hash value
then at that index we will have two node values, and so we will join them using the next_node pointer like a singly
linkedlist, and this is how we store/put a key, value pair.

Now to get a value from a key, we find the hash value, and get the index of the array, and then if the index already
contains a node, then we will iterate through it to find the node with matching key and finally return its value.


"""


class Node:
    def __init__(self, key, val, next_node=None):
        self.key = key
        self.val = val
        self.next_node = next_node


class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]

    def put(self, key, val):
        table_idx = self.get_hash(key)
        node = self.table[table_idx]
        if node:
            prev = node
            while node:
                if node.key == key:
                    node.val = val
                    return
                else:
                    prev = node
                    node = node.next_node
            prev.next_node = Node(key, val)
        else:
            self.table[table_idx] = Node(key, val)

    def get(self, key):
        table_idx = self.get_hash(key)
        node = self.table[table_idx]
        if node:
            while node:
                if node.key == key:
                    return node.val
                node = node.next_node

        return None

    def get_hash(self, key):
        return key % self.size


if __name__ == "__main__":
    my_hash_table = MyHashTable(50)
    my_hash_table.put(5, "hello")
    my_hash_table.put(10, "world")
    my_hash_table.put(20, "Saurav")
    my_hash_table.put(20, "Gupta")

    print(my_hash_table.get(5))
    print(my_hash_table.get(10))
    print(my_hash_table.get(20))
