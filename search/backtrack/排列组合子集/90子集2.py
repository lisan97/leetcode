class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        track = []
        self.n = len(nums)
        #先排序，让相同的元素靠在一起
        nums.sort()
        self.backtrack(nums,track,0)
        return self.res

    def backtrack(self,nums,track,start):
        self.res.append(track[:])
        for i in range(start,self.n):
            #剪枝逻辑，值相同的相邻树枝，只遍历第一条
            if i > start and nums[i] == nums[i-1]:
                continue
            track.append(nums[i])
            self.backtrack(nums,track,i+1)
            track.pop()