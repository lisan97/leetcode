class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        #找到链表中点作为父节点，然后以链表头结点和中点的下一个节点为开头，递归生成左右子树
        if not head:
            return head
        slow = head
        fast = head
        pre = None#记录中点的前一个节点，从而断开连接
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(val=slow.val)
        if pre:
            pre.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root