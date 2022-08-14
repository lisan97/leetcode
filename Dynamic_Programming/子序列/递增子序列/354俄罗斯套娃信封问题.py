class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        #先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序
        #因为两个宽度相同的信封不能相互包含的，逆序排序保证在 w 相同的数对中最多只选取一个
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        #之后把所有的 h 作为一个数组，在这个数组上计算 LIS 的长度
        nums = [i[1] for i in envelopes]
        n = len(nums)
        '''
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
        '''
        length = 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            left = 0
            right = length
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == length:
                length += 1
            dp[left] = num
        return length


if __name__ == '__main__':
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    #3
    print(Solution().maxEnvelopes(envelopes))