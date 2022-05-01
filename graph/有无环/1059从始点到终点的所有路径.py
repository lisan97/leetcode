class Solution(object):
    def leadsToDestination(self,n, edges, source, destination):
        '''
        1.终点只有一个并且是destination
        2.没有环
        '''
        self.graph = self.buildgraph(n,edges)
        self.isCycle = False
        self.errorDes = False
        self.visited = [False] * n
        self.onPath = [False] * n
        self.traverse(source,destination)
        return not self.isCycle and not self.errorDes

    def buildgraph(self,n,edges):
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
        return graph

    def traverse(self,s,destination):
        #出现终点，但不是destination
        if not self.graph[s] and s != destination:
            self.errorDes = True
        #出现环
        if self.onPath[s]:
            self.isCycle = True
        if self.visited[s] or self.isCycle or self.errorDes:
            return
        self.visited[s] = True
        self.onPath[s] = True
        for node in self.graph[s]:
            self.traverse(node,destination)
        self.onPath[s] = False

if __name__ == '__main__':
    n = 4
    edges = [[0,1],[0,2],[1,3],[2,3]]
    source = 0
    destination = 3
    print(Solution().leadsToDestination(n,edges,source,destination))