class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 用邻接表记录每个出发地能去哪些地方
        # 将每个列表变为优先队列，这样能够使目的地按照字典顺序排序，且能够在O(1)时间内返回最小的那个目的地
        # 从JFK开始dfs，在一个地点没有目的地时，将该地点加入到list里
        # 最后翻转list，返回
        from collections import defaultdict
        from heapq import *
        self.dic = defaultdict(list)
        self.stack = []
        for i in range(len(tickets)):
            self.dic[tickets[i][0]].append(tickets[i][1])
        for k in self.dic:
            heapify(self.dic[k])
        self.dfs("JFK")
        self.stack.reverse()
        return self.stack

    def dfs(self, cur):
        while self.dic[cur]:
            tmp = heappop(self.dic[cur])
            self.dfs(tmp)
        self.stack.append(cur)