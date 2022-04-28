# 字典+双向链表 链表的每个node存放频率freq以及对应的keys;字典存放key->Node
class Node:
    def __init__(self, key="", count=0, next=None, pre=None):
        self.keys = set([key])
        self.count = count
        self.next = next
        self.pre = pre


class Doublelist:
    def __init__(self):
        self.head = Node()  # head和tail都是哨兵结点
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def addNodeAfter(self, newNode, prevNode):
        prevNode.next.pre = newNode
        newNode.next = prevNode.next
        newNode.pre = prevNode
        prevNode.next = newNode

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre


class AllOne(object):

    def __init__(self):
        self.freqMap = Doublelist()
        self.keyMap = {}

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        # key不在map中
        if key not in self.keyMap:
            # 链表为空，或头结点的count>1
            if self.freqMap.head.next == self.freqMap.tail or self.freqMap.head.next.count > 1:
                node = Node(key, 1)
                self.freqMap.addNodeAfter(node, self.freqMap.head)
                self.keyMap[key] = node
            # 存在count=1的node
            else:
                self.freqMap.head.next.keys.add(key)
                self.keyMap[key] = self.freqMap.head.next
        # key在map中
        else:
            # cur.next为空或cur.next.count > cur.count+1
            cur = self.keyMap[key]
            if cur.next == self.freqMap.tail or cur.count + 1 < cur.next.count:
                node = Node(key, cur.count + 1)
                self.freqMap.addNodeAfter(node, cur)
                self.keyMap[key] = node
            else:
                # 存在cur.next
                cur.next.keys.add(key)
                self.keyMap[key] = cur.next
            cur.keys.remove(key)
            if not cur.keys:
                self.freqMap.remove(cur)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        cur = self.keyMap[key]
        # key只出现一次
        if cur.count == 1:
            self.keyMap.pop(key)
        else:
            # 若cur.pre为空或cur.pre.count < cur.count-1
            if cur.pre == self.freqMap.head or cur.pre.count < cur.count - 1:
                node = Node(key, cur.count - 1)
                self.freqMap.addNodeAfter(node, cur.pre)
                self.keyMap[key] = node
            else:
                cur.pre.keys.add(key)
                self.keyMap[key] = cur.pre
        cur.keys.remove(key)
        if not cur.keys:
            self.freqMap.remove(cur)

    def getMaxKey(self):
        """
        :rtype: str
        """
        return next(iter(self.freqMap.tail.pre.keys)) if self.freqMap.head.next != self.freqMap.tail else ''

    def getMinKey(self):
        """
        :rtype: str
        """
        return next(iter(self.freqMap.head.next.keys)) if self.freqMap.head.next != self.freqMap.tail else ''
