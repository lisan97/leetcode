class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph = self.buildGraph(numCourses, prerequisites)
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses
        # 记录后序遍历结果
        self.res = []
        # 记录是否存在环
        self.hasCycle = False
        # 遍历图
        for i in range(numCourses):
            self.traverse(i)
        # 有环图无法进行拓扑排序
        if self.hasCycle:
            return []
        # 逆后序遍历结果即为拓扑排序结果
        return self.res[::-1]

    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for req in prerequisites:
            graph[req[1]].append(req[0])
        return graph

    def traverse(self, s):
        if self.onPath[s]:
            self.hasCycle = True

        if self.visited[s] or self.hasCycle:
            return
        # 前序遍历位置
        self.visited[s] = True
        self.onPath[s] = True
        for node in self.graph[s]:
            self.traverse(node)
        # 后序遍历位置
        self.res.append(s)
        self.onPath[s] = False

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph, degree = self.buildGraph(numCourses,prerequisites)
        start = [i for i in range(numCourses) if degree[i] == 0]
        for node in start:
            for nextnode in graph[node]:
                degree[nextnode] -= 1
                if degree[nextnode] == 0:
                    start.append(nextnode)
        return start if len(start) == numCourses else []

    def buildGraph(self,numCourses,prerequisites):
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for line in prerequisites:
            graph[line[1]].append(line[0]) #统计依赖关系图
            degree[line[0]] += 1 #统计入度
        return graph, degree