class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        '''
        visited数组是用来剪枝的，在代码中是全局变量，并且只赋值true，而没有像onPath一样有回溯操作（即onPath【s】=false），举个例值，有a，b两个节点都有一条到c的路径，那么a判断之后被标记了visited【s】=true，b再去遍历的时候可以直接返回。
        onPath是记录回溯的路径的，是检查环是否存在的重要标志！
        经过测试，只有OnPath没有visited，在100个节点的时候就会超时。
        '''
        self.graph = self.buildGraph(numCourses, prerequisites)
        # 记录图中是否有环
        self.hascycle = False
        # 防止走回头路进入死循环，并不用来判断环
        self.visited = [False] * numCourses
        # 记录一次 traverse 递归经过的节点
        self.onPath = [False] * numCourses
        for i in range(numCourses):
            # 以每个节点为起始遍历一遍
            self.traverse(i)
        return not self.hascycle

    def traverse(self, s):
        if self.onPath[s]:
            # 出现环
            self.hascycle = True

        if self.visited[s] or self.hascycle:
            # 如果已经找到了环，也不用再遍历了
            return

        self.visited[s] = True
        self.onPath[s] = True
        for node in self.graph[s]:
            self.traverse(node)
        self.onPath[s] = False

    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for req in prerequisites:
            graph[req[1]].append(req[0])
        return graph