class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #1.通过快慢指针找到链表中点
        #2.对链表进行归并排序
        return self.sort(head,None)

    #维持一个左闭右开区间[head,tail)
    def sort(self,head,tail):
        if not head:
            return head
        #从中点将链表断开
        if head.next == tail:
            head.next = None
            return head
        #找到mid
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        #以中点为分界，将链表拆分成两个子链表，对两个子链表分别排序，然后合并
        return self.merge(self.sort(head,slow),self.sort(slow,tail))
    #leetcode 21合并两个有序链表
    def merge(self,list1,list2):
        dummy  = ListNode()
        p = dummy
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return dummy.next