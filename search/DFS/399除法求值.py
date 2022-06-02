class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #其实就是看能否通过连除的关系找到分子和分母，找到的话就有答案，没找到就是-1，防止走回头路，加入visited集合
        from collections import defaultdict
        self.graph = self.buildGraph(equations,values)
        ans = []
        for s,t in queries:
            self.visited = set()
            self.visited.add(s)
            ans.append(self.dfs(s,t))
        return ans
    #构建加权边
    def buildGraph(self,equations,values):
        graph = defaultdict(dict)
        for (a,b), v in zip(equations,values):
            graph[a][b] = v
            graph[b][a] = 1/ v
        return graph

    def dfs(self,s,t):
        if s not in self.graph:
            return - 1
        if s == t:
            return 1
        #dfs
        for node in self.graph[s]:
            if node == t:
                return self.graph[s][node]
            if node not in self.visited:
                self.visited.add(node)
                v = self.dfs(node,t)
                if v != -1:
                    return self.graph[s][node] * v
        return -1