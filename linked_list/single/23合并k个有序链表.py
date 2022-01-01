import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #虚拟头结点
        dummy = ListNode()
        p = dummy
        #优先级队列，最小堆
        head = []
        #将 k 个链表的头结点加入最小堆
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head,(lists[i].val,i))
                lists[i] = lists[i].next
        while head:
            #获取最小节点，接到结果链表中
            val, index = heapq.heappop(head)
            p.next = ListNode(val)
            #p 指针不断前进
            p = p.next
            if lists[index]:
                #如果该链表还有结点，则将其加入最小堆
                heapq.heappush(head,(lists[index].val,index))
                lists[index] = lists[index].next
        return dummy.next