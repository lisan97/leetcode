#O(nlogn)
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        给出一个已经排好序的测试样例 [0, 1, 2, 6, 8]
        通过对数据的观察，可以得知，对首尾的两个数 0,8 最小的移动次数就是在 [0, 8] 之间任意找一个数，他们的固定移动次数都是 8；如果尝试在这个区间外找一个数来计算移动次数，如找 -1，则 0和8 的移动次数则为 10
        同理，我们对 1和6 进行最小次数移动的话， [1, 6] 中的任意数，他们固定移动 5次
        最后剩下一个中间的数 2，不移动的话，最小次数为 0
        如果是偶数的话，则取中间两个数的任意一个都行
        '''
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        res = 0
        for i in range(n):
            res += abs(nums[i]-median)
        return res

#快速选择,O(n)
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        给出一个已经排好序的测试样例 [0, 1, 2, 6, 8]
        通过对数据的观察，可以得知，对首尾的两个数 0,8 最小的移动次数就是在 [0, 8] 之间任意找一个数，他们的固定移动次数都是 8；如果尝试在这个区间外找一个数来计算移动次数，如找 -1，则 0和8 的移动次数则为 10
        同理，我们对 1和6 进行最小次数移动的话， [1, 6] 中的任意数，他们固定移动 5次
        最后剩下一个中间的数 2，不移动的话，最小次数为 0
        如果是偶数的话，则取中间两个数的任意一个都行
        '''
        import random
        random.shuffle(nums)
        n = len(nums)
        target = n // 2
        left = 0
        right = n-1
        while left <= right:
            p = self.partition(nums,left,right)
            if p == target:
                median = nums[p]
                break
            elif p < target:
                left = p + 1
            else:
                right = p - 1
        res = 0
        for i in range(n):
            res += abs(nums[i]-median)
        return res

    def partition(self,nums,left,right):
        pivot = nums[left]
        i = left + 1
        j = right
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
        nums[left] = nums[j]
        nums[j] = pivot
        return j