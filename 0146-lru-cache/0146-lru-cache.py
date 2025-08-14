class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.head.next=self.tail
        self.tail.prev=self.head
    
    def _remove(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
    
    def _insert(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

        

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        node=Node(key,value)
        self._insert(node)
        self.cache[key]=node

        if len(self.cache)>self.capacity:
            lru=self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)