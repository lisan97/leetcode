class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        self.target = len(graph) - 1
        self.path = []
        self.traverse(graph, 0)
        return self.res

    def traverse(self, graph, s):
        # 添加节点 s 到路径
        self.path.append(s)
        if s == self.target:
            # 到达终点
            # 向 res 中添加 path 时需要拷贝一个新的列表，不能直接append(path)否则最终 res 中的列表都是空的。
            self.res.append(self.path[:])
            self.path.pop()
            return
        # 递归每个相邻节点
        for node in graph[s]:
            self.traverse(graph, node)
        # 从路径移出节点 s
        self.path.pop()