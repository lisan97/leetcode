#动态规划O(N²)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

#二分查找O(NlogN)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #牌堆数初始化为 0
        piles = 0
        top = [0]*len(nums)
        for i in range(len(nums)):
            #要处理的扑克牌
            poker = nums[i]
            left = 0
            right = piles
            #搜索左侧边界的二分查找：如果当前牌有多个堆可供选择，则选择最左边的那一堆放置。
            while left < right:
                mid = (left+right) // 2
                if top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid
            #没找到合适的牌堆，新建一堆
            if left == piles:
                piles += 1
            #把这张牌放到牌堆顶
            top[left] = poker
        #牌堆数就是 LIS 长度
        return piles