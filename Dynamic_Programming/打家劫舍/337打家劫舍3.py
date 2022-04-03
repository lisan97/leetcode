# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # 状态：在哪个节点
        # 选择：抢该点or抢该节点的子节点
        # dp(node)代表以该节点为root节点能抢到的最高金额
        # base case:node=None时 return 0
        # 状态转移:抢当前节点然后抢下下家；不抢当前节点，抢下家
        self.memo = {}
        return self.dp(root)

    def dp(self, node):
        if not node:
            return 0
        if node in self.memo:
            return self.memo[node]
        # 抢，然后去下下家
        left = self.dp(node.left.left) + self.dp(node.left.right) if node.left else 0
        right = self.dp(node.right.left) + self.dp(node.right.right) if node.right else 0
        do = node.val + left + right
        # 不抢，然后去下家
        not_do = self.dp(node.left) + self.dp(node.right)
        res = max(do, not_do)
        self.memo[node] = res
        return res