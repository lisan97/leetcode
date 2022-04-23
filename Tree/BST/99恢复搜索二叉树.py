class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        #用两个变量first,second来记录需要交换的节点
        self.firstNode = None
        self.secondNode = None
        #设置一个 prev 指针，记录当前节点中序遍历时的前节点
        self.pre = TreeNode(val=float('-inf'))
        self.traverse(root)
        if self.firstNode and self.secondNode:
            self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val
        return root

    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        # 如果遍历整个序列过程中只出现了一次次序错误，说明就是这两个相邻节点需要被交换；
        # 如果出现了两次次序错误，那就需要交换这两个节点
        if root.val < self.pre.val:
            if not self.firstNode:
                self.firstNode = self.pre
            self.secondNode = root
        self.pre = root
        self.traverse(root.right)