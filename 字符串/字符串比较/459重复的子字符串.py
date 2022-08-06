class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        #两层循环
        for i in range(1,n//2+1):
            found = True
            if not n % i:
                for j in range(i,n):
                    if s[j] != s[j-i]:
                        found = False
                        break
                if found:
                    return True
        return False