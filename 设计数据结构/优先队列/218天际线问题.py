class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from heapq import *
        #每个长方形的左右两个顶点都需要扫描一下
        #右端点：此时意味着之前某一条往右延展的线结束了，这时候需要将高度出队，需重新计算此时的最高高度
        events = sorted([(L, -H, R) for L, R, H in buildings] + list(set((R, 0, 0) for _, R, _ in buildings)))
        res = [[0,0]]
        hq = [[0,float('inf')]] #[H,R]
        #从左往右遍历
        for L,H,R in events:
            #现在的坐标已经和这个点(右坐标)没有重合了
            while L >= hq[0][1]:
                heappop(hq)
            if H:
                heappush(hq,[H,R])
            #如果最高的高度改变, 将[x, height]记录在res中
            if res[-1][1] != -hq[0][0]:
                res.append([L,-hq[0][0]])
        return res[1:]