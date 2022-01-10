class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # 记录重复的子树根节点
        self.res = []
        # 记录所有子树以及出现的次数
        self.memo = {}
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return '#'
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        # 左右子树加上自己，就是以自己为根的二叉树序列化结果
        subtree = left + ',' + right + ',' + str(root.val)
        #记录有没有出现过，一般都用hashMap
        freq = self.memo.setdefault(subtree, 0)
        # 多次重复也只会被加入结果集一次
        if freq == 1:
            self.res.append(root)
        # 给子树对应的出现次数加一
        self.memo[subtree] += 1
        return subtree