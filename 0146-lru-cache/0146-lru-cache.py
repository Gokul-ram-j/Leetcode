class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail

    def insert(self,node):
        
        self.head.next.prev=node
        node.next=self.head.next
        self.head.next=node
        node.prev=self.head
        self.head.next=node
        
    
    def delete(self,node):

        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key in self.map:
            self.delete(self.map[key])
            self.insert(self.map[key])
            return self.map[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.map:
           self.delete(self.map[key])

        node=Node(key,value)
        self.insert(node) 
        self.map[key]=node

        if len(self.map)>self.capacity:
            lru_node=self.tail.prev
            self.delete(lru_node)
            del self.map[lru_node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)