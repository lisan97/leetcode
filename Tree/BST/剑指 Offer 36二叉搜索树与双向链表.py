class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        '''
        root.left指向前一个节点，root.right指向后一个节点
        初始化一个pre，遍历的时候，若self.pre为空时，说明是头结点，赋给self.head
        完成递归遍历后self.pre指向尾结点，将其与self.head连起来
        '''
        if not root:
            return
        self.pre = None
        self.traverse(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head

    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        if not self.pre:
            self.head = root
        else:
            self.pre.right = root
            root.left = self.pre
        self.pre = root
        self.traverse(root.right)