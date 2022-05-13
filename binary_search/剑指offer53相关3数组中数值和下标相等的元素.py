''' 
单调递增的数组里的每个元素都是整数且唯一。
请实现一个函数找出数组任意一个数值等于其下标的元素
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == mid:
                return mid
            elif nums[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        return - 1
    
if __name__ == '__main__':
    nums = [-3,-1,1,3,5]
    print(Solution().missingNumber(nums))