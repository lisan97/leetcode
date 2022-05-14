class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1.先翻转所有字符顺序
        # 2.再分别翻转每个单词内字符的顺序
        s = self.reverse(s)
        s = ' '.join([self.reverse(c) for c in s.split()])
        return s

    def reverse(self, s):
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.strip().split()[::-1])