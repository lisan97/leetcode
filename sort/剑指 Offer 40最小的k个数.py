#大顶堆 O(nlogk),不修改数据集，适用于海量数据(不需要一下子全读进来)
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import *
        hq = []
        for i in range(len(arr)):
            heappush(hq,-arr[i])
            if len(hq) > k:
                heappop(hq)
        return [-i for i in hq]

#patition函数的特点，左边的数都小于p，只要p是第k-1个，就可以直接输出arr[:p+1]
#O(n)
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        #partition
        n = len(arr)
        if k > n:
            return -1
        if n <= 1:
            return arr
        import random
        random.shuffle(arr)
        l = 0
        r = n - 1
        p = self.partition(arr,l,r)
        while p != k-1:
            if p < k-1:
                l = p + 1
            else:
                r = p - 1
            p = self.partition(arr,l,r)
        return arr[:p+1]


    def partition(self,nums,l,r):
        if l == r:
            return l
        p = nums[l]
        i = l + 1
        j = r
        done = False
        while not done:
            while i <= j and nums[i] <= p:
                i += 1
            while i <= j and nums[j] >= p:
                j -= 1
            if i > j:
                done = True
            else:
                nums[i], nums[j] = nums[j], nums[i]
        nums[l] = nums[j]
        nums[j] = p
        return j