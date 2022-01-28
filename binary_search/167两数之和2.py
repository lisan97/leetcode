class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            num = numbers[left] + numbers[right]
            if num == target:
                #题目要求的索引是从 1 开始的
                return [left+1,right+1]
            elif num < target:
                #让 sum 大一点
                left += 1
            else:
                #让 sum 小一点
                right -= 1