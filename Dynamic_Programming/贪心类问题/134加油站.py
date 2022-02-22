#图像解法：找最低点
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        #相当于图像中的坐标点和最低点
        total,minsum,start=0,float('inf'),0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < minsum:
                #经过第 i 个站点后，使 sum 到达新低
                #所以站点 i + 1 就是最低点（起点）
                start = i+1
                minsum = total
        #总油量小于总的消耗，无解
        if total < 0:
            return -1
        #环形数组特性
        return 0 if start == n else start

#贪心解法：如果我发现从 i 出发无法走到 j，那么 i 以及 i, j 之间的所有站点都不可能作为起点。
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        total = 0
        for i in range(n):
            total += gas[i] - cost[i]
        if total < 0:
            return -1
        tank = 0
        start = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                #无法从 start 走到 i
                #那么 start 以及 start, i 之间的所有站点都不可能作为起点，从i+1开始
                tank = 0
                start = i+1
        return 0 if start == n else start