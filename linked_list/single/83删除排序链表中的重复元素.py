# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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