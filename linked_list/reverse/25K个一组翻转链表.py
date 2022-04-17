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
        newHead = self.reverse(a, b) #newHead是[a,b)区间的最后一个，现在变成了头结点，a变成了最后一个
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k) #然后继续以b为头结点开始翻转下一个区间，并将a连上下一个区间的newHead
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