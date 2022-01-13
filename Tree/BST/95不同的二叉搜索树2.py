class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        #构造闭区间 [1, n] 组成的 BST
        return self.build(1,n)

    def build(self,start,end):
        res = []
        #base case
        if start > end:
            return [None]
        #列举每一个节点为根节点时的情况
        for i in range(start,end+1):
            #列举左右子树所有的可能组合
            leftTree = self.build(start,i-1)
            rightTree = self.build(i+1,end)
            #给 root 节点穷举所有左右子树的组合：
            #从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
            for left in leftTree:
                for right in rightTree:
                    root = TreeNode(val=i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res