class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        dummy = ListNode(0,head)
        p2 = dummy
        i = 0
        #p1 先走 k 步
        for i in range(n):
            p1 = p1.next
        #p1 和 p2 同时走 n - k 步
        while p1:
            p1 = p1.next
            p2 = p2.next
        #p2 现在指向第 n - k 个节点
        p2.next = p2.next.next
        return dummy.next