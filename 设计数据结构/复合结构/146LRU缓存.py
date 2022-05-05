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

#字典+双向链表 字典存放key->Node
class Node:
    def __init__(self,key,val,next=None,pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre

class Doublelist:
    def __init__(self):
        self.head = Node(-1,-1)#head和tail都是哨兵结点
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def addFirst(self, x):
        #在头部加入一个Node
        x.next = self.head.next
        x.pre = self.head
        self.head.next.pre = x
        self.head.next = x
        self.size += 1

    def remove(self, x):
        #删除一个Node
        x.next.pre = x.pre
        x.pre.next = x.next
        self.size -= 1

    def removeLast(self):
        #删除最后一个结点，并返回
        if self.size == 0:
            return None
        delNode = self.tail.pre
        self.remove(delNode)
        return delNode

    def getSize(self):
        return self.size

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.cache = Doublelist()

    def get(self, key: int) -> int:
        if key in self.map:
            val = self.map[key].val
            self.put(key,val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key,value)
        if key in self.map:
            self.cache.remove(self.map[key])
        else:
            if self.cache.getSize() == self.capacity:
                delNode = self.cache.removeLast()
                self.map.pop(delNode.key)
        self.cache.addFirst(newNode)
        self.map[key] = newNode

#自己实现哈希链表(linked hash map)
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
        # 如果 key 存在，先通过哈希表定位，再移到尾部
        node = self.cache[key]
        self.moveToTail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DlinkedNode(key,value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的尾部
            self.addToTail(node)
            self.size += 1
            if self.size > self.capacity:
                 # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeHead()
                # 删除哈希表中对应的项
                del self.cache[removed.key]
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到尾部
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