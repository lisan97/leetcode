class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                #要么删除左要么删除右
                return self.isPalindrome(s,left+1,right) or self.isPalindrome(s,left,right-1)
        return True


    def isPalindrome(self,s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True