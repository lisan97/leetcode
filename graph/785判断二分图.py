#DFS
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.graph = graph
        n = len(graph)
        self.visited = [False] * n
        #记录图中节点的颜色，false 和 true 代表两种不同颜色
        self.color = [False] * n
        self.isBiGraph = True
        for i in range(n):
            #将base case写在循环内
            if not self.visited[i]:
                self.traverse(i)
        return self.isBiGraph

    def traverse(self,s):
        #如果已经确定不是二分图了，就不用浪费时间再递归遍历了
        if not self.isBiGraph:
            return
        self.visited[s] = True
        for node in self.graph[s]:
            #将base case写在循环内
            if not self.visited[node]:
                #相邻节点 w 没有被访问过
                #那么应该给节点 w 涂上和节点 v 不同的颜色
                self.color[node] = not self.color[s]
                #继续遍历 w
                self.traverse(node)
            else:
                #相邻节点 w 已经被访问过
                #根据 v 和 w 的颜色判断是否是二分图
                if self.color[node] == self.color[s]:
                    self.isBiGraph = False
#BFS
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.graph = graph
        n = len(graph)
        self.visited = [False] * n
        #记录图中节点的颜色，false 和 true 代表两种不同颜色
        self.color = [False] * n
        self.isBiGraph = True
        for i in range(n):
            #将base case写在循环内
            if not self.visited[i]:
                self.bfs(i)
        return self.isBiGraph

    def bfs(self,s):
        queue = [s]
        self.visited[s] = True
        while queue and self.isBiGraph:
            w = queue.pop()
            #从节点w 向所有相邻节点扩散
            for node in self.graph[w]:
                if not self.visited[node]:
                    self.color[node] = not self.color[w]
                    self.visited[node] = True
                    queue.append(node)
                else:
                    if self.color[node] == self.color[w]:
                        self.isBiGraph = False