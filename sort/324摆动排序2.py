class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        tmp = nums[:]
        tmp.sort()
        n = len(nums)
        x = (n+1)//2
        j = x - 1
        k = n - 1
        for i in range(0,n,2):
            nums[i] = tmp[j]
            if i + 1 < n:
                nums[i+1] = tmp[k]
            j -= 1
            k -= 1