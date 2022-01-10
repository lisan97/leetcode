class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #利用 BST 的中序遍历递增序列的特性
        #记录结果
        self.res = -1
        #记录当前元素的排名
        self.rank = 0
        self.traverse(root,k)
        return self.res

    def traverse(self,root,k):
        if not root:
            return None
        self.traverse(root.left,k)
        self.rank += 1
        #找到第 k 小的元素
        if self.rank == k:
            self.res = root.val
            return
        self.traverse(root.right,k)

#follow up
#如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
#AVL 树(时间复杂度：预处理的时间复杂度为 O(N)，其中 N 是树中结点的总数。插入、删除和搜索的时间复杂度均为 O(log N)。)