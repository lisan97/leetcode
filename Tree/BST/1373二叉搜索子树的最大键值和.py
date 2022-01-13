class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = 0
        self.traverse(root)
        return self.maxSum

    def traverse(self,root):
        '''
        当前节点需要知道三件事：
        1、左右子树是否是 BST。
        2、左子树的最大值和右子树的最小值。
        3、左右子树的节点值之和。
        '''
        if not root:
            return [1,float('inf'),float('-inf'),0]
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        res = []
        '''
        res[0] 记录以 root 为根的二叉树是否是 BST，若为 1 则说明是 BST，若为 0 则说明不是 BST；
        res[1] 记录以 root 为根的二叉树所有节点中的最小值；
        res[2] 记录以 root 为根的二叉树所有节点中的最大值；
        res[3] 记录以 root 为根的二叉树所有节点值之和。
        '''
        if (left[0] == 1) and (right[0]==1) and (root.val > left[2]) and (root.val < right[1]):
            res.append(1)
            res.append(min(left[1],root.val))
            res.append(max(right[2],root.val))
            res.append(left[3]+right[3]+root.val)
            self.maxSum = max(self.maxSum,res[3])
        else:
            res = [0]
        return res