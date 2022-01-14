class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#后序遍历
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        '''
        #代表None
        ,为分隔符
        '''
        if not root:
            return '#'
        leftTree = self.serialize(root.left)
        rightTree = self.serialize(root.right)
        #后序遍历形式
        Tree = leftTree +',' +rightTree +',' +str(root.val)
        return Tree

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        root = self.helpdeserialize(nodes)
        return root

    def helpdeserialize(self, nodes):
        if not nodes:
            return None
        #从后往前取节点，顺序：根-右-左
        last = nodes.pop()
        if last == '#':
            return None
        root = TreeNode(val=int(last))
        #先构造右子树，后构造左子树
        root.right = self.helpdeserialize(nodes)
        root.left = self.helpdeserialize(nodes)
        return root

#先序遍历
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        leftTree = self.serialize(root.left)
        rightTree = self.serialize(root.right)
        Tree = str(root.val) + ',' + leftTree + ',' + rightTree
        return Tree

    def deserialize(self, data):
        from collections import deque
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = deque(data.split(','))
        root = self.helpdeserialize(nodes)
        return root

    def helpdeserialize(self, nodes):
        if not nodes:
            return None
        first = nodes.popleft()
        if first == '#':
            return None
        root = TreeNode(val=int(first))
        root.left = self.helpdeserialize(nodes)
        root.right = self.helpdeserialize(nodes)
        return root

#层次遍历
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        if not root:
            return '#'
        res = ''
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # 把对空指针的检验从「将元素加入队列」的时候改成了「从队列取出元素」的时候
            if not node:
                res += '#,'
                continue
            res = res + str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res.strip(',')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == '#':
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        # 队列queue记录父节点
        queue = deque([root])
        # 每一个非空节点都会对应两个子节点
        # 反序列化的思路也是用队列进行层级遍历，同时用索引 i 记录对应子节点的位置
        i = 0
        while i < len(nodes) - 1:
            parent = queue.popleft()
            # 父节点对应的左侧子节点的值
            i += 1
            left = nodes[i]
            if left != '#':
                parent.left = TreeNode(int(left))
                queue.append(parent.left)
            else:
                parent.left = None
            # 父节点对应的右侧子节点的值
            i += 1
            right = nodes[i]
            if right != '#':
                parent.right = TreeNode(int(right))
                queue.append(parent.right)
            else:
                parent.right = None

        return root