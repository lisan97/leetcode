class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        #前导空格
        s = s.lstrip()
        #为空
        if not s:
            return 0
        #判断正负号
        i = 0
        n = len(s)
        if s[i] == '+':
            sign = 1
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        elif s[i].isdigit():
            sign = 1
        else:
            return 0
        #对后续数字字符进行转换
        num = 0
        while i < n and s[i].isdigit():
            num = 10 * num + ord(s[i]) - ord('0')
            i += 1
        return max(min(num * sign,2147483647),-2147483648)