class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        有一个整型数组，需要对其进行排序，排序规则为nums[0]<=nums[1]>=nums[2]<=nums[3]...
        """
        n = len(nums)
        for i in range(n-1):
            #奇数
            if i % 2 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            #偶数
            if not i % 2 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

if __name__ == '__main__':
    nums = [i for i in range(6)]
    Solution().wiggleSort(nums)
    print(nums)