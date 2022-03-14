class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        #给剩余孩子里最小饥饿度的孩子分配最小的能饱腹的饼干
        #具体实现：把孩子和饼干分别排序
        g.sort()
        s.sort()
        m = len(g)
        n = len(s)
        res = 0
        i = 0
        j = 0
        while i < m and j < n:
            if s[j] >= g[i]:
                i += 1
                res += 1
            j += 1
        return res