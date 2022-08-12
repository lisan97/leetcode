class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        add = n - k % n
        if add == n:
            return head
        # 将链表连成环
        cur.next = head
        #找到最后一个结点
        while add:
            cur = cur.next
            add -= 1
        # 新头部结点
        newHead = cur.next
        # 最后一个节点，断开
        cur.next = None
        return newHead