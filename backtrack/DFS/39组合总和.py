class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        track = []
        self.n = len(candidates)
        candidates.sort()
        self.backtrack(candidates,track,0,target)
        return self.res

    def backtrack(self,candidates,track,start,remain):
        if remain == 0:
            self.res.append(track[:])
        for i in range(start,self.n):
            #超过目标和，停止向下遍历
            if candidates[i] > remain:
                break
            track.append(candidates[i])
            #让每个元素被重复使用，则下一层从i开始遍历
            self.backtrack(candidates,track,i,remain-candidates[i])
            track.pop()