class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tmp = sorted(nums)
        n = len(nums)
        left = (n-1)//2 #左半部分是较小元素
        right = n - 1 #右半部分是较大元素
        #两个指针都指向两部分的右侧，先插left后插right来达到一大一小的目的
        for i in range(n):
            if not i % 2:
                nums[i] = tmp[left]
                left -= 1
            else:
                nums[i] = tmp[right]
                right -= 1