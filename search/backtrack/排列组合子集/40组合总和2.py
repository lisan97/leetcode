class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        track = []
        self.n = len(candidates)
        self.target = target
        #先排序，让相同的元素靠在一起
        candidates.sort()
        self.backtrack(candidates,track,0,target)
        return self.res

    def backtrack(self,candidates,track,start,remain):
        #base case，达到目标和，找到符合条件的组合
        if remain == 0:
            self.res.append(track[:])
        for i in range(start,self.n):
            #如果candidates[i]大于remain，直接break，因为这是有序数组，后面的值肯定都大于remain
            if candidates[i] > remain:
                break
            #剪枝逻辑，值相同的树枝，只遍历第一条
            if i > start and candidates[i] == candidates[i-1]:
                continue
            track.append(candidates[i])
            self.backtrack(candidates,track,i+1,remain-candidates[i])
            track.pop()

if __name__ == '__main__':
    candidates = [-10, 1, 2, 7, 6, 1, 5]
    target = -8
    print(Solution().combinationSum2(candidates,target))