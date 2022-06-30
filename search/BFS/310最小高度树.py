#会超时
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        neighbor = defaultdict(list)
        for node1, node2 in edges:
            neighbor[node1].append(node2)
            neighbor[node2].append(node1)
        maxh = n
        res = []
        for i in range(n):
            h = self.bfs(i, neighbor)
            if h == maxh:
                res.append(i)
            elif h < maxh:
                maxh = h
                res = [i]
            else:
                continue
        return res

    def bfs(self, s, neighbor):
        queue = deque([s])
        visited = set([s])
        step = 0
        while queue:
            sz = len(queue)
            for _ in range(sz):
                node = queue.popleft()
                for nextnode in neighbor[node]:
                    if nextnode not in visited:
                        queue.append(nextnode)
                        visited.add(nextnode)
            step += 1
        return step

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        '''
        越是靠里面的节点越有可能是最小高度树。
        所以，我们可以这样想，我们可以倒着来。
        我们从边缘开始，先找到所有出度为1的节点，然后把所有出度为1的节点进队列，然后不断地bfs，最后找到的就是两边同时向中间靠近的节点，那么这个中间节点就相当于把整个距离二分了，那么它当然就是到两边距离最小的点啦，也就是到其他叶子节点最近的节点了。
        '''
        from collections import defaultdict,deque
        if n == 1:
            return [0]
        neighbor = defaultdict(list)
        degree = defaultdict(int)
        for node1,node2 in edges:
            degree[node1] += 1
            degree[node2] += 1
            neighbor[node1].append(node2)
            neighbor[node2].append(node1)

        queue = deque([])

        for node in degree:
            if degree[node] == 1:
                queue.append(node)

        while queue:
            sz = len(queue)
            res = []
            for _ in range(sz):
                node = queue.popleft()
                #我们每次循环都会新建一个list，所以最后保存的就是最后一个状态下的叶子节点，
                #这也是很多题解里面所说的剪掉叶子节点的部分，你可以想象一下图，每层遍历完，
                #都会把该层（也就是叶子节点层）这一层从队列中移除掉，
                #不就相当于把原来的图给剪掉一圈叶子节点，形成一个缩小的新的图吗
                res.append(node)
                #把当前节点的相邻接点都拿出来，
                #把它们的出度都减1，因为当前节点已经不存在了，所以，
                #它的相邻节点们就有可能变成叶子节点
                for nextnode in neighbor[node]:
                    degree[nextnode] -= 1
                    if degree[nextnode] == 1:
                        #如果是叶子节点我们就入队
                        queue.append(nextnode)
        return res