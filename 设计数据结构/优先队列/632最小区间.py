class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from heapq import *
        #维护一个hq,一个res和一个cur
        hq = []
        res = [10**5,-10**5]
        for i in range(len(nums)):
            heappush(hq,(nums[i][0],i,0))
            res[0] = min(res[0],nums[i][0])
            res[1] = max(res[1],nums[i][0])
        cur = res[:]
        while hq:
            num, i, j = heappop(hq)
            if j == len(nums[i]) - 1:
                break
            heappush(hq,(nums[i][j+1],i,j+1))
            cur[0] = hq[0][0]
            cur[1] = max(cur[1],nums[i][j+1])
            if (cur[1]-cur[0]) < (res[1]-res[0]):
                res = cur[:]
        return res