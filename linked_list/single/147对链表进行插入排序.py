class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        cur = head #cur 指针负责扫描整个链表
        while cur and cur.next:
            if cur.val <= cur.next.val: #符合递增，继续往前
                cur = cur.next
            else:
                tmp = cur.next #cur.next比cur小，则需要改变其位置，先保存下来
                cur.next = cur.next.next #删除cur.next
                pre = dummy
                while pre.next.val <= tmp.val: #使用pre从头开始扫描，寻找tmp的合适位置
                    pre = pre.next
                #此时pre比tmp小，pre.next比tmp大，将tmp插在他们之间
                tmp.next = pre.next
                pre.next = tmp
        return dummy.next