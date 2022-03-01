class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        for i in range(n):
            for j in range(1,n-i):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return nums

if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    print(Solution().sortArray(nums))