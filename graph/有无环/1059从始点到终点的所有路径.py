class Solution(object):
    def leadsToDestination(self,n, edges, source, destination):
        '''
        1.终点只有一个
        2.没有环
        '''
        self.graph = self.buildGraph(n,edges)
        num = 0
        for i in range(n):
            if not self.graph[i]:
                num += 1
            if num > 1:
                return False
        self.isCycle = False
        self.visited = [False] * n
        self.onPath = [False] * n
        for i in range(n):
            self.traverse(i)
        return not self.isCycle

    def buildgraph(self,n,edges):
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
        return graph

    def traverse(self,s):
        if self.onPath[s]:
            self.isCycle = True
        if self.visited[s] or self.isCycle:
            return
        self.visited[s] = True
        self.onPath[s] = True
        for node in self.graph[s]:
            self.traverse(node)
        self.onPath[s] = False