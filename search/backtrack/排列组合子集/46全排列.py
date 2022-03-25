class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #记录结果
        self.res = []
        #记录路径
        track = []
        used = [False] * len(nums)
        self.backtrack(nums,track,used)
        return self.res

    def backtrack(self,nums,track,used):
        #结束条件：nums 中的元素全都在 track 中出现
        if len(track) == len(nums):
            # 向 res 中添加 path 时需要拷贝一个新的列表，不能直接append(path)否则最终 res 中的列表都是空的。
            self.res.append(track[:])
            return
        #选择列表：nums 中不存在于 track 的那些元素
        for i in range(len(nums)):
            if used[i]:
                continue
            #做选择
            used[i] = True
            track.append(nums[i])
            #进入下一层决策树
            self.backtrack(nums,track)
            #取消选择
            used[i] = False
            track.pop()