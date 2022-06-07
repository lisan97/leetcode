class Binary_Tree():
    def __init__(self, root=None, left=None, right=None, parent=None):
        self.root = root
        self.left = left
        self.right = right
        self.parent = parent

#中序遍历的下一个节点
def find_next_node(pNode):
    # 是否非空节点
    if not pNode:
        return
    #1.有右子树的情况，下一个节点是右子树最左的叶子节点
    #2.没有右子树的情况，如果是父节点的左子节点，则下一个节点是父节点
    #3.没有右子树，且是父节点的右子节点，则沿父节点的指针一直往上遍历，直到找到一个当前节点是它父节点的左子节点的节点，如果不存在，就是没有下一个节点
    parent = pNode.parent
    # 1.有右子树的情况，下一个节点是右子树最左的叶子节点
    if pNode.right:
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode
    #没有右子树的情况
    else:
        #如果是父节点的左子节点
        if parent and parent.left == pNode:
            return parent
        #如果是父节点的右子节点
        elif parent and parent.right == pNode:
            #当前节点是它父节点的左子节点的节点
            while parent.parent:
                if parent.parent.left == parent:
                    return parent.parent
                else:
                    parent = parent.parent