class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#迭代BFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        #从上到下遍历二叉树的每一层
        while queue:
            size = len(queue)
            tmp = []
            #这个for循环是为了从左到右遍历每一层的每个节点，将这层的节点放进一个list
            #如果不需要放，只是print的话，则不需要这个for循环
            for _ in range(size):
                cur = queue.popleft()
                #将本层的节点放入tmp
                tmp.append(cur.val)
                #将下一层节点放入队列
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp)
        return res

#迭代BFS不用for循环
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque()
        queue.append((root,0))
        #从上到下遍历二叉树的每一层
        while queue:
            cur,depth = queue.popleft()
            # 当遍历到一个新的深度 level，而最终结果 res 中还没有创建 level 对应的列表时，应该在 res 中新建一个列表用来保存该 level 的所有节点
            if len(res) == depth:
                res.append([])
            res[depth].append(cur.val)
            if cur.left:
                queue.append((cur.left,depth+1))
            if cur.right:
                queue.append((cur.right,depth+1))

        return res

#递归DFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = []
        self.traverse(root, 0)
        return self.res

    def traverse(self, node, level):
        # 当遍历到一个新的深度 level，而最终结果 res 中还没有创建 level 对应的列表时，应该在 res 中新建一个列表用来保存该 level 的所有节点
        if len(self.res) == level:
            self.res.append([])
        # 将当前节点值加入到该层的list中
        self.res[level].append(node.val)
        # 递归处理左右子树
        if node.left:
            self.traverse(node.left, level + 1)
        if node.right:
            self.traverse(node.right, level + 1)