class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        #状态：第i个pair
        #dp[i]:截止到第i个pair的最长数对链的长度
        #因为是拿第i个pair的第1个数去和前面每个pair的第二个数比，并且第一个数比第二个数字，因此可以先根据第二个数排序，然后用二分查找左边界
        n = len(pairs)
        if n == 1:
            return 1
        pairs.sort(key=lambda x:x[1])
        dp = [0] * n
        dp[0] = 1
        for i in range(1,n):
            num = pairs[i][0]
            for j in range(i):
                if num > pairs[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

#二分，时间o(nlogn)，看见o(n)
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        #状态：第i个pair
        #dp[i]:截止到第i个pair的最长数对链的长度
        #因为是拿第i个pair的第1个数去和前面每个pair的第二个数比，并且第一个数比第二个数字，因此可以先根据第二个数排序，然后用二分查找右边界
        n = len(pairs)
        if n == 1:
            return 1
        pairs.sort(key=lambda x:x[1])
        dp = [0] * n
        length = 0
        for i in range(n):
            left = 0
            right = length
            #和300题不同的是，每次拿pairs[i][0]和每个堆的头(pairs[x][1])比较
            while left < right:
                mid = (left+right) // 2
                if dp[mid] < pairs[i][0]:
                    left = mid + 1
                else:
                    right = mid
            #如果比所有堆的头都大，将pairs[i][1]作为新的一堆的头，因此只有满足条件时才更新堆的头
            if left == length:
                length += 1
                dp[left] = pairs[i][1]
        return length

#区间问题，贪心，时间o(nlogn)，空间o(1)
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        #其实也是区间问题，寻找最多的不重叠子区间，用贪心来做
        n = len(pairs)
        if n == 1:
            return 1
        pairs.sort(key=lambda x:x[1])
        num = 1
        last = pairs[0][1]
        for i in range(1,n):
            if pairs[i][0] > last:
                num += 1
                last = pairs[i][1]
        return num