class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#一次遍历「穿针引线」反转链表（头插法）
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        #如果要翻转的区间包含了原始链表的第一个位置，那么使用 dummy 就可以维护整个翻转的过程更加通用
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for _ in range(left-1):
            pre = pre.next
        cur = pre.next
        for _ in range(right-left):
            next = cur.next #next为cur的下一个
            cur.next = next.next #1将cur.next指向next.next，如果先定义next.next指向pre.next,则会丢失原next.next结点
            next.next = pre.next #2将next.next指向pre.next，如果先定义pre.next指向next，则会丢失原pre.next结点
            pre.next = next
        return dummy.next

#迭代
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # 例子1->2->3->4->5   1->4->3->2->1
        if not head or not head.next:
            return head
        dummy = ListNode() #防止从第一个开始翻转，没有pre节点的情况，因此弄一个虚拟头结点
        dummy.next = head
        pre = dummy
        # 1.先将结点移动到a的前一个
        for _ in range(left - 1):
            pre = pre.next
        # 2.确定[a,b)这个区间
        #pre:1
        #a:2
        a = b = pre.next
        for _ in range(right - left + 1):
            b = b.next
        # 3.翻转[a,b)这个区间
        #b:5
        newHead = self.reverse(a, b)
        #newHead:4
        #1->4
        pre.next = newHead
        # 4.将a(现在已是[a,b)区间的尾结点)指向b
        #2->5
        a.next = b
        return dummy.next

    def reverse(self, a, b):
        """
        翻转a到b之间的节点
        将head改为a,将cur != None改为cur != b
        """
        pre = None
        cur = a
        while cur != b:
            #在改变cur.next前，存下之前的cur.next
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        # 返回反转后的头结点
        return pre

#递归
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        #例子1->2->3->4->5   1->4->3->2->1
        if not head or not head.next:
            return head
        if left == 1:
            #返回的是翻转后的头结点4，然后被1连上
            return self.reverseN(head,right)
        #如果把 head.next 的索引视为1，反转的区间应该是从第left-1个元素开始的，就这样前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next,left-1,right-1)
        return head

    #反转前n个元素
    def reverseN(self,head, n):
        #当n减少到1时，也就是反转这个结点的本身，即直接返回该结点
        if n == 1:
            #记录第 n + 1 个节点
            self.successor = head.next
            return head
        #以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next,n-1)
        #将head连到head.next后
        head.next.next = head
        #让反转之后的 head 节点和后面的节点连起来
        head.next = self.successor
        return last