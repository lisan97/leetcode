# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#多次调用getRandom的情况
#先遍历一遍链表，得到链表的总长度 n，再生成一个 [1,n]之间的随机数为索引，然后找到索引对应的节点
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        import random
        self.length = 0
        self.head = head
        while head:
            head = head.next
            self.length += 1

    def getRandom(self):
        """
        :rtype: int
        """
        i = random.randint(0,self.length-1)
        p = self.head
        while i:
            p = p.next
            i -= 1
        return p.val

#follow up如果链表非常大且长度未知，并且希望一次能够完成get random
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        import random
        self.head = head


    def getRandom(self):
        """
        :rtype: int
        """
        i = 0
        p = self.head
        res = 0
        #while 循环遍历链表
        while p:
            #生成一个 [0, i] 之间的整数
            #这个整数等于 0 的概率就是 1/i
            n = random.randint(0,i)
            if n == 0:
                res = p.val
            i += 1
            p = p.next
        return res