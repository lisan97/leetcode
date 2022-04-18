class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #用一个p_odd负责遍历索引为奇数结点，一个p_even负责遍历索引为偶数结点，同时记录下第一个偶数结点
        #遍历完后，将最后一个奇数结点的next指向第一个偶数结点
        if not head or not head.next:
            return head
        p_odd = head
        p_even = head.next
        p_even_first = p_even
        while p_odd.next and p_even.next:
            p_odd.next = p_odd.next.next
            p_odd = p_odd.next
            p_even.next = p_even.next.next
            p_even = p_even.next
        p_odd.next = p_even_first
        return head