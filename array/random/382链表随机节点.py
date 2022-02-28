# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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