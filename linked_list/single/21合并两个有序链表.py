class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = ListNode()
        p = dummy
        while list1 and list2:
            # 比较 p1 和 p2 两个指针
            # 将值较小的的节点接到 p 指针
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            #p指针不断前进
            p = p.next
        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return dummy.next
