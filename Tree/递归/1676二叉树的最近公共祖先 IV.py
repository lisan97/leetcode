class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
给你输入一个包含若干节点的列表nodes（这些节点都存在于二叉树中），让你算这些节点的最近公共祖先。
'''
class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        :rtype: TreeNode
        """
        self.nodes = set(nodes)
        return self.find(root)
        
    def find(self,root):
        if not root:
            return None
        #前提：这些节点必定存在于二叉树中
        if root.val in self.nodes:
            return root
        left = self.find(root.left)
        right = self.find(root.right)
        if left and right:
            return root
        return left if left else right