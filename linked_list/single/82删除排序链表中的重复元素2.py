class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #维护三个指针pre,cur,nex
        #当cur.val != nex.val时，三个指针同时移动
        #当cur.val == nex.val时，只往前移动nex
        if not head or not head.next:
            return head
        dummy = ListNode(val=-101)
        dummy.next = head
        pre = dummy
        cur = head
        nex = head.next
        while nex:
            if cur.val != nex.val:
                pre = pre.next
                cur = cur.next
                nex = nex.next
            else:
                while nex and cur.val == nex.val:
                    nex = nex.next
                pre.next = nex
                cur = nex
                if nex:
                    nex = nex.next
        return dummy.next