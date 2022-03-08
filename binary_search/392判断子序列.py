#双指针,O(n)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m

#哈希+二分，O(m*logn)
#follow up:如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列（可以假定 s 较短，t 很长）
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        dic = defaultdict(list)
        m = len(s)
        n = len(t)
        for i in range(n):
            dic[t[i]].append(i)
        # t 上的指针
        j = 0
        for i in range(m):
            c = s[i]
            #整个 t 压根儿没有字符 c
            if c not in dic:
                return False
            index = self.binarySearch(dic[c],j)
            #二分搜索区间中没有找到字符 c
            if index == len(dic[c]):
                return False
            #向前移动指针 j
            j = dic[c][index] + 1
        return True
    #查找左侧边界的二分查找，查找大于target的最小索引
    def binarySearch(self,nums,target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left