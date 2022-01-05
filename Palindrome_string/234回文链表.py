class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#空间复杂度O(n)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]

#空间复杂度O(1)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        p1 = p2 = head
        #通过 双指针技巧 中的快慢指针来找到链表的中点
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        #如果fast指针没有指向null，说明链表长度为奇数，slow还要再前进一步
        if p2:
            p1 = p1.next
        #从slow开始反转后面的链表
        p1 = self.reverse(p1)
        #开始比较回文串
        while p1:
            if head.val != p1.val:
                return False
            p1 = p1.next
            head = head.next
        return True

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre