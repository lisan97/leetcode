#堆，O(NlogK)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import *
        pq = []
        for i in range(len(nums)):
            heappush(pq,nums[i])
            if len(pq) > k:
                heappop(pq)
        return pq[0]

#快速选择，O(N)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random
        #首先随机打乱数组
        random.shuffle(nums)
        lo = 0
        hi = len(nums) - 1
        #索引转化(升序)
        k = len(nums) - k
        while lo <= hi:
            #在 nums[lo..hi] 中选一个分界点
            p = self.partition(nums,lo,hi)
            if p < k:
                #第 k 大的元素在 nums[p+1..hi] 中
                lo = p + 1
            elif p > k:
                #第 k 大的元素在 nums[lo..p-1] 中
                hi = p - 1
            else:
                #找到第 k 大元素
                return nums[p]
        return -1

    def partition(self,nums, lo, hi):
        if lo == hi:
            return lo
        pivot = nums[lo]
        i = lo+1
        j = hi
        done = False
        while not done:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] >= pivot:
                j -= 1
            if i > j:
                done = True
            else:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        tmp = nums[lo]
        nums[lo] = nums[j]
        nums[j] = tmp
        return j