from collections import defaultdict
class Node(object):
    def __init__(self,key,val,prev=None,next=None,freq=0):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = freq

    def insert(self,next):
        next.prev = self
        next.next = self.next
        self.next.prev = next
        self.next = next

def create_linked_list():
    head = Node(0,0)
    tail = Node(0,0)
    head.next = tail
    tail.prev = head
    return (head,tail)

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.miniFreq = 0
        self.keyMap = {}
        self.freqMap = defaultdict(create_linked_list)

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
            #如果双链表为空，则在freqMap里去掉该freq key
            if node.prev is self.freqMap[node.freq][0] and node.next is self.freqMap[node.freq][-1]:
                self.freqMap.pop(node.freq)
        return node.key

    def increase(self, node):
        #增加node的freq
        node.freq += 1
        #删去原有node
        self.delete(node)
        #在freq+1后的key的双链表中插入node至尾部
        self.freqMap[node.freq][-1].prev.insert(node)
        #插入的是新node的情况
        if node.freq == 1:
            self.miniFreq = 1
        elif self.miniFreq == node.freq -1:
            #之前的freq的双链表为空的情况
            head, tail = self.freqMap[node.freq - 1]
            if head.next is tail:
                self.miniFreq = node.freq


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        self.increase(node)
        return node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #capacity有可能为0
        if self.capacity != 0:
            #key已存在
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
                self.increase(node)
            #key不存在
            else:
                #容量已满
                if self.size == self.capacity:
                    #淘汰freq最小且最久为使用的key
                    deleted = self.delete(self.freqMap[self.miniFreq][0].next)
                    self.size -= 1
                    self.keyMap.pop(deleted)
                #插入key和value
                node = Node(key,value)
                self.keyMap[key] = node
                self.increase(node)
                self.size += 1