class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #遍历并打印每个节点的坐标
        #用一个字典记录每列的节点的行和值
        from collections import defaultdict
        self.dic = defaultdict(list)
        self.mincol = 1001
        self.maxcol = -1001
        self.traverse(root,0,0)
        res = []
        for k in range(self.mincol,self.maxcol+1):
            res.append([v[1] for v in sorted(self.dic[k],key=lambda x:(x[0],x[1]))])
        return res

    def traverse(self,root,row,col):
        if not root:
            return
        self.mincol = min(self.mincol,col)
        self.maxcol = max(self.maxcol,col)
        self.dic[col].append((row,root.val))
        self.traverse(root.left,row+1,col-1)
        self.traverse(root.right,row+1,col+1)