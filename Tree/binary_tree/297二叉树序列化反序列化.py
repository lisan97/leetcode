class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
