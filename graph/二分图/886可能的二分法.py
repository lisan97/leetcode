#DFS
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        self.graph = self.buildGraph(n, dislikes)
        self.visited = [False] * n
        self.color = [False] * n
        self.isBiGraph = True
        for i in range(n):
            if not self.visited[i]:
                self.traverse(i)
        return self.isBiGraph

    def buildGraph(self, n, dislikes):
        graph = [[] for _ in range(n)]
        for req in dislikes:
            # 「无向图」相当于「双向图」
            # 图节点编号为 1...n，序号为0...n-1
            graph[req[0] - 1].append(req[1] - 1)
            graph[req[1] - 1].append(req[0] - 1)
        return graph

    def traverse(self, s):
        if not self.isBiGraph:
            return
        self.visited[s] = True
        for node in self.graph[s]:
            if not self.visited[node]:
                self.color[node] = not self.color[s]
                self.traverse(node)
            else:
                if self.color[node] == self.color[s]:
                    self.isBiGraph = False

#BFS
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        self.graph = self.buildGraph(n, dislikes)
        self.visited = [False] * n
        self.color = [False] * n
        self.isBiGraph = True
        for i in range(n):
            if not self.visited[i]:
                self.bfs(i)
        return self.isBiGraph

    def buildGraph(self, n, dislikes):
        graph = [[] for _ in range(n)]
        for req in dislikes:
            # 「无向图」相当于「双向图」
            # 图节点编号为 1...n，序号为0...n-1
            graph[req[0] - 1].append(req[1] - 1)
            graph[req[1] - 1].append(req[0] - 1)
        return graph

    def bfs(self, s):
        queue = [s]
        self.visited[s] = True
        while queue and self.isBiGraph:
            w = queue.pop()
            for node in self.graph[w]:
                if not self.visited[node]:
                    self.color[node] = not self.color[w]
                    self.visited[node] = True
                    queue.append(node)
                else:
                    if self.color[w] == self.color[node]:
                        self.isBiGraph = False