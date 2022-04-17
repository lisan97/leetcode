class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        2个一组翻转
        '''
        a,b = head,head
        for _ in range(2):
            if not b:
                return head
            b = b.next
        newHead = self.reverse(a,b)
        a.next = self.swapPairs(b)
        return newHead

    def reverse(self,a,b):
        pre = None
        cur = a
        while cur != b:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre