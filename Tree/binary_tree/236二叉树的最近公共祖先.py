class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # base case
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 1.p和q都不在以root为根的树
        if not left and not right:
            return None
        # 若一个节点能够在它的左右子树中分别找到p和q，则该节点一定是pq的公共祖先，又因为是后序遍历位置，从下往上，所以第一个公共节点就是为LCA节点
        # 并且因为两个点都已经找到了，再返回上一层父节点的时候，另一边一定为None，所以就一直会将该节点返回至递归结束
        if left and right:
            return root
        # 3.p和q只有一个存在于root为根的树中
        return left if left else right