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
        count = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                #若和上一个字符串不同，则之前相同且连续的长度变为和当前字符串连续的不同数字的长度
                #和当前位置数字相同且连续的长度回到1
                pre = cur
                cur = 1
            #若不同数字的连续长度大于等于当前数字的连续长度，
            #则说明存在一个且只存在一个以当前数字结尾的满足条件的子字符串。
            if pre >= cur:
                count += 1
        return count