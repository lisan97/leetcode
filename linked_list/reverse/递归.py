class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#翻转整个链表
def reverseList(head:ListNode):


    return


#翻转前N个链表
def reverseN(head:ListNode,n):
    if not head or not head.next:
        return head

    return

#翻转链表某个区间
def reverseGroup(a:ListNode,b:ListNode):
    #翻转区间[a,b)
    #调用时还需维护一个pre(a的前一个)用来和newHead相连

    return