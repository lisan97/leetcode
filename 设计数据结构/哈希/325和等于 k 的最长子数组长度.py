class Solution(object):
    def maxSubArrayLen(self, nums,k):
        n = len(nums)
        dic = {}
        total = 0
        maxlen = 0
        for i in range(n):
            total += nums[i]
            if total == k:
                maxlen = max(maxlen,i+1)
            if (total-k) in dic:
                maxlen = max(maxlen,i-dic[total-k])
            if total not in dic:
                dic[total] = i
        return maxlen if maxlen > 0 else 0

if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    k = 3
    print(Solution().maxSubArrayLen(nums,k))
