# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        if not root:
            return 0
        queue = deque([root])
        step = 1
        while queue:
            sz = len(queue)
            #将当前队列中的所有节点向四周扩散
            for _ in range(sz):
                node = queue.popleft()
                #断是否到达终点
                if not node.left and not node.right:
                    return step
                #将 cur 的相邻节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            step += 1
        return step