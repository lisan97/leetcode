
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        #用哈希表记录每一个节点对应新节点的创建情况
        self.dic = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        '''
        注意一个节点可能被多个其他节点指向，因此我们可能递归地多次尝试拷贝某个节点，
        为了防止重复拷贝，我们需要首先检查当前节点是否被拷贝过，
        如果已经拷贝过，我们可以直接从哈希表中取出拷贝后的节点的指针并返回即可
        '''
        if head in self.dic:
            return self.dic[head]
        node = Node(head.val)
        self.dic[head] = node #将原有节点和新节点的对应关系添加到哈希表中
        '''
        我们检查「当前节点的后继节点」和「当前节点的随机指针指向的节点」的创建情况。
        如果这两个节点中的任何一个节点的新节点没有被创建，我们都立刻递归地进行创建。
        当我们拷贝完成，回溯到当前层时，我们即可完成当前节点的指针赋值。
        '''
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node