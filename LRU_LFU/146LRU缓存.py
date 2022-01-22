#使用orderdict
class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.queue = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.queue:
            self.queue.move_to_end(key)
            return self.queue[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.queue:
            self.queue[key] = value
            self.queue.move_to_end(key)
        else:
            if len(self.queue.keys()) == self.capacity:
                self.queue.popitem(last=False)
                self.queue[key] = value
            else:
                self.queue[key] = value
#自己实现哈希链表
class DlinkedNode:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToTail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DlinkedNode(key,value)
            self.cache[key] = node
            self.addToTail(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeHead()
                del self.cache[removed.key]
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToTail(node)

    def addToTail(self,node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToTail(self,node):
        self.removeNode(node)
        self.addToTail(node)

    def removeHead(self):
        node = self.head.next
        self.removeNode(node)
        return node