class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        i = 0
        index = 0
        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[index] = chars[i]
            index += 1
            diff = j - i
            if diff > 1:
                for c in str(diff):
                    chars[index] = c
                    index += 1
            i = j
        return index