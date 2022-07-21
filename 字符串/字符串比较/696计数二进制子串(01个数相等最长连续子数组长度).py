class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        从左往右遍历数组，记录和当前位置数字相同且连续的长度，以及其之前连续的不同数字的长度
        '''
        pre = 0
        cur = 1
        max_length = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                pre = cur
                cur = 1
            if pre >= cur:
                max_length = max(max_length,2*cur)
        return max_length

if __name__ == '__main__':
    s = '0100001000011111000011100001010010010100'
    print(Solution().countBinarySubstrings(s))