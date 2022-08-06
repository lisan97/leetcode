# Definition for singly-linked list.
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
        if not head or not head.next:
            return head
        p = head
        while p and p.next:
            #如果p和p.next相等，将p链接到p.next.next
            if p.val == p.next.val:
                p.next = p.next.next
            #否则p往前挪一位
            else:
                p = p.next
        return head

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #维护两个指针pre,cur
        #当pre.val != cur时，同时移动
        #当pre.val == cur时，只往前移动cur
        dummy = ListNode(val=-101)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if pre.val != cur.val:
                cur = cur.next
                pre = pre.next
            else:
                while cur and pre.val == cur.val:
                    cur = cur.next
                pre.next = cur
        return dummy.next