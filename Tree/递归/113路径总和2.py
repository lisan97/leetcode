class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        '''
        二叉树版回溯算法
        '''
        if not root:
            return []
        self.res = []
        track = []
        self.traverse(root,track,targetSum)
        return self.res

    def traverse(self,root,track,targetSum):
        track.append(root.val)
        targetSum -= root.val
        #必须是根节点到叶子节点的路径总和
        if targetSum == 0 and not root.left and not root.right:
            self.res.append(track[:])
            track.pop()
            return
        if root.left:
            self.traverse(root.left,track,targetSum)
        if root.right:
            self.traverse(root.right,track,targetSum)
        track.pop()