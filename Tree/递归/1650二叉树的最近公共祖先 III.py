#这次输入的二叉树节点比较特殊，包含指向父节点的指针：
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

#这道题其实不是公共祖先的问题，而是单链表相交的问题，你把parent指针想象成单链表的next指针
class Solution(object):
    def lowestCommonAncestor(self, p,q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode or None
        """
        i = p
        j = q
        while i != j:
            if not i:
                i = q
            else:
                i = i.parent
            if not j:
                j = p
            else:
                j = j.parent
        return i