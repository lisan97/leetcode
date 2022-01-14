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
        self.pre = TreeNode(val=float('-inf'))
        self.traverse(root)
        if self.firstNode and self.secondNode:
            self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val
        return root

    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        #第一个节点，是第一个按照中序遍历时候前一个节点大于后一个节点，我们选取前一个节点
        #第二个节点，是在第一个节点找到之后，后面出现前一个节点大于后一个节点，我们选择后一个节点
        if root.val < self.pre.val:
            if not self.firstNode:
                self.firstNode = self.pre
            self.secondNode = root
        self.pre = root
        self.traverse(root.right)