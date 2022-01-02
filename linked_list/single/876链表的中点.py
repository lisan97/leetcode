class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p1 = p2 = head
        #快指针走到末尾时停止
        while p1 and p1.next:
            #慢指针走一步，快指针走两步
            p1 = p1.next.next
            p2 = p2.next
        return p2