class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 区间 [a, b) 包含 k 个待反转元素
        a = b = head
        for _ in range(k):
            # 不足 k 个，不需要反转，base case
            if not b:
                return head
            b = b.next
        # 反转前 k 个元素
        newHead = self.reverse(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return newHead

    def reverse(self, a, b):
        """
        翻转a到b之间的节点
        将head改为a,将cur != None改为cur != b
        """
        pre = None
        cur = a
        while cur != b:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        # 返回反转后的头结点(newHead)
        return pre