class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        使用层次遍历，每层从左往右遍历，第一个就是最左边的节点
        用一个字典保存每层最左边的那个点
        '''
        from collections import deque
        q = deque([root])
        i = 0
        dic = {}
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if i not in dic:
                    dic[i] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i += 1
        return dic[i-1]