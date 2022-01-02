class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        p1 = p2 = head
        #快指针走到末尾时停止
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            #快慢指针相遇，说明含有环
            if p1 == p2:
                return True
        return False