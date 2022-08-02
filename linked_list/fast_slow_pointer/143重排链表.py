class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #找链表中点
        #以中点开始反转链表
        #然后交叉插入节点
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        newHead = self.reverseList(mid)
        while head and newHead:
            headtmp = head.next
            newHeadtmp = newHead.next

            head.next = newHead
            head = headtmp

            newHead.next = head
            newHead = newHeadtmp

    def reverseList(self,head):
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre