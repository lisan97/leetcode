class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        先排序
        统计0的个数，除0之外相邻数的差值
        如果相邻数的差值小于等于0的个数，则可以；否则不行
        若遇到除0之外重复的数字，则肯定不行
        '''
        nums.sort()
        zero_count = 0
        diff_count= 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                continue
            if i == 0:
                continue
            if nums[i] == nums[i-1]:
                return False
            if nums[i-1] != 0:
                diff_count += nums[i] - nums[i-1] - 1
        return zero_count >= diff_count