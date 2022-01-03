class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#翻转整个链表
def reverseList(head:ListNode):
    if not head or not head.next:
        return head
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


#翻转前N个链表
def reverseN(head:ListNode,n):
    if not head or not head.next:
        return head
    pre = None
    cur = head
    for _ in range(n):
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    head.next = cur
    return pre

#翻转链表某个区间
def reverseGroup(a:ListNode,b:ListNode):
    #翻转区间[a,b)
    #调用时还需维护一个pre(a的前一个)用来和newHead相连
    pre = None
    cur = a
    while cur != b:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    # 返回反转后的头结点(newHead)
    return pre




