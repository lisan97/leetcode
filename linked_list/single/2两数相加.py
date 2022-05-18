class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #因为链表和要求的结果都是逆序，所以可以直接开始加
        dummy = ListNode()
        p = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            val = val1 + val2 + carry
            carry = val // 10
            cur = val % 10
            node = ListNode(cur)
            p.next = node
            p = p.next
        return dummy.next