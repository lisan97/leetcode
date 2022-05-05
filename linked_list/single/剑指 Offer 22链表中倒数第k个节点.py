class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return
        slow = head
        fast = head
        for _ in range(k):
            #万一k大于链表长度
            if not fast:
                return
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow