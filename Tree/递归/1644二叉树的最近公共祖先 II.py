class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
给你输入一棵不含重复值的二叉树，已经两个节点p和q，
如果p或q不存在于树中，则返回空指针，否则的话返回p和q的最近公共祖先节点。
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p,q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode or None
        """
        self.foundp = False
        self.foundq = False
        res = self.find(root,p,q)
        #p 和 q 都存在二叉树中，才有公共祖先
        if self.foundp and self.foundq:
            return res
        else:
            return None

        
    def find(self,root,p,q):
        if not root:
            return None
        left = self.find(root.left,p,q)
        right = self.find(root.right,p,q)
        #后序位置，判断当前节点是不是 LCA 节点
        if left and right:
            return root
        #后序位置，判断当前节点是不是目标值，找到了的话记录一下
        if root == p:
            self.foundp = True
            return root
        if root == q:
            self.foundq = True
            return root
        return left if left else right