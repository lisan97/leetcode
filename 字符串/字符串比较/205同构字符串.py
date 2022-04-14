class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        将问题转化一下：记录两个字符串每个位置的字符第一次出现的位置，如果两个字
        符串中相同位置的字符与它们第一次出现的位置一样，那么这两个字符串同构。
        '''
        from collections import defaultdict
        first_index_s = defaultdict(int)
        first_index_t = defaultdict(int)
        for i in range(len(s)):
            if first_index_s[s[i]] != first_index_t[t[i]]:
                return False
            #因为默认就是0，所以得用i+1，把在第一个位置出现和没出现过区分开来
            first_index_s[s[i]],first_index_t[t[i]]=i+1,i+1
        return True