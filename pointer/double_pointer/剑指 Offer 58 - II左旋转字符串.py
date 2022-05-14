class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        from collections import deque
        s = deque(list(s))
        for _ in range(n):
            s.append(s.popleft())
        return ''.join(s)


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        # 将旋转的部分看成前一个单词，不旋转的部分看成后一个单词
        s = self.reverse(s[:n]) + self.reverse(s[n:])
        return self.reverse(s)

    def reverse(self, s):
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)