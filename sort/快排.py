class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import random
        #首先随机打乱数组
        random.shuffle(nums)
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, lo, hi):
        if lo >= hi:
            return
        #通过交换元素构建分界点索引 p
        p = self.partition(nums, lo, hi)
        #现在 nums[lo..p-1] 都小于 nums[p]，
        #且 nums[p+1..hi] 都大于 nums[p]
        self.quicksort(nums, lo, p - 1)
        self.quicksort(nums, p + 1, hi)

    def partition(self, nums, lo, hi):
        if lo == hi:
            return lo
        #将 nums[lo] 作为默认分界点 pivot
        pivot = nums[lo]
        i = lo + 1
        j = hi
        done = False
        while not done:
            #保证 nums[lo..i] 都小等于 pivot
            while i <= j and nums[i] <= pivot:
                i += 1
            #保证 nums[j..hi] 都大等于 pivot
            while i <= j and nums[j] >= pivot:
                j -= 1
            if i > j:
                done = True
            else:
                #如果走到这里，一定有：
                # nums[i] > pivot && nums[j] < pivot
                # 所以需要交换 nums[i] 和 nums[j]，
                # 保证 nums[lo..i] <= pivot <= nums[j..hi]
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        #将 pivot 值交换到正确的位置
        tmp = nums[lo]
        nums[lo] = nums[j]
        nums[j] = tmp
        #现在 nums[lo..j-1] <= nums[j] <= nums[j+1..hi]
        return j