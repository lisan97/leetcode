class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #如果遍历完还没相遇，两个都是None，也能输出
        p1 = headA
        p2 = headB
        while p1 != p2:
            #p1 走一步，如果走到 A 链表末尾，转到 B 链表
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            #p2 走一步，如果走到 B 链表末尾，转到 A 链表
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        return p1