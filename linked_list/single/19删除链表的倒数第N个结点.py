class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        先遍历一遍链表，记下链表的长度
        然后从dummpy开始往后走length-n次，到达导数第n-1个结点
        '''
        p = head
        length = 0
        while p:
            p = p.next
            length += 1
        #添加一个哑节点（dummy node），它的next 指针指向链表的头节点。这样一来，我们就不需要对头节点进行特殊的判断了
        dummy = ListNode()
        dummy.next = head
        p = dummy
        for _ in range(length - n):
            p = p.next
        p.next = p.next.next

        return dummy.next

#一次遍历
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        弄两个快慢指针，让快指针先走n步，然后开始同时走，
        当快指针遍历完链表时，慢指针正好在导数第n个结点
        '''
        if not head or n == 0:
            return
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = head
        for _ in range(n):
            # 万一k大于链表长度
            if not fast:
                return
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next