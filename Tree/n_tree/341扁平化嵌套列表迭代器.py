# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

#转化成了一个 N 叉树的遍历问题，深度优先搜索，把每个intger放进一个双向队列
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        from collections import deque
        self.res = deque([])
        for node in nestedList:
            self.traverse(node)

    def traverse(self, root):
        if root.isInteger():
            self.res.append(root.getInteger())
        for child in root.getList():
            self.traverse(child)

    def next(self):
        """
        :rtype: int
        """
        return self.res.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.res:
            return True
        return False


# 迭代时不需要全部展开，只需要把 当前list 的所有元素放入 list 中
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        from collections import deque
        self.queue = deque(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # 调用hasNext时，如果nestedList的第一个元素是列表类型，则不断展开这个元素，直到第一个元素是整数类型。
        while self.queue:
            cur = self.queue[0]
            if cur.isInteger():
                return True
            self.queue.popleft()
            tmp = cur.getList()
            for i in range(len(tmp) - 1, -1, -1):
                self.queue.appendleft(tmp[i])
        return False