class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        '''
        1.None
        2.头结点
        3.尾结点
        4.中间结点
        '''
        if not head:
            return
        dummy = ListNode()#防止是删除头结点
        dummy.next = head
        p = head
        pre = dummy
        while p:
            if p.val == val:
                pre.next = p.next
                break
            pre = p
            p = p.next
        return dummy.next