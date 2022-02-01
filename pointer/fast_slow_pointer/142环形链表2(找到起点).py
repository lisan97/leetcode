class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = p2 = head

        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                break
        #fast 遇到空指针说明没有环
        if not p1 or not p1.next:
            return None
        #重新指向头结点
        p2 = head
        #快慢指针同步前进，相交点就是环起点
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2