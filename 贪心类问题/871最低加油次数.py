class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        #状态加i次油
        #dp[i]表示加i次油能跑的最远距离
        #base case:dp[0] = startFuel
        #状态转移：dp[j+1] = max(dp[j+1], dp[j]+stations[j][1]) if dp[j] >= stations[j][0]
        n = len(stations)
        dp = [0] * (n+1)
        dp[0] = startFuel
        for i in range(n):
            for j in range(i,-1,-1):
                #必须能达到此加油站才能更新dp[j]
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j]+stations[i][1])
        for i in range(n+1):
            if dp[i] >= target:
                return i
        return -1

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        '''
        维护一个最大堆
        当路过一个加油站先不加油，将该加油站压入堆中
        当油不够用时，弹出最大的那个加油站
        当油不够用且堆为空时，返回-1
        '''
        from heapq import *
        hq = []
        cur = startFuel
        count = 0
        stations.append([target,0])
        for i in range(len(stations)):
            while cur < stations[i][0]:
                if not hq:
                    return -1
                fuel = - heappop(hq)
                cur += fuel
                count += 1
            heappush(hq,-stations[i][1])
        return count