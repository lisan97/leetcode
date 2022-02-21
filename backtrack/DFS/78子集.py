class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        如果 A = subset([1,2]) ，那么：
        subset([1,2,3])
        = A + [A[i].add(3) for i = 1..len(A)]
        '''
        self.res = []
        track = []
        self.backtrack(nums,track,0)
        return self.res

    def backtrack(self,nums,track,start):
        #收集子集
        self.res.append(track[:])
        #既然是无序，取过的元素不会重复取，写回溯算法的时候，for就要从startIndex开始，而不是从0开始！
        for i in range(start,len(nums)):
            track.append(nums[i])
            self.backtrack(nums,track,i+1)
            track.pop()