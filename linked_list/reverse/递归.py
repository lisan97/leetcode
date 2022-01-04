class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#翻转整个链表
def reverseList(head:ListNode):
    if not head or not head.next:
        return head
    last = reverseList(head.next)
    head.next.next = head
    head.next = None

    return last


#翻转前N个链表
def reverseN(head:ListNode,n):
    if n == 1:
        suceesor = head.next
        return head
    last = reverseN(head.next,n-1)
    head.next.next = head
    head.next = suceesor
    return last
