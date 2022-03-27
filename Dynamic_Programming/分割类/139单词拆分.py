class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #状态：在字符串第几位
        #选择：用哪个word
        #dp[i]在字符串第i位是否能拼接成功
        #dp[i] = dp[i] or dp[i-len1] or dp[i-len2] or ...
        from collections import defaultdict
        dic = defaultdict(list)
        for word in wordDict:
            dic[len(word)].append(word)
        len_list = sorted(list(dic.keys()))
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            for length in len_list:
                #因为len_list是排序的，如果该length超出长度，后面的肯定也超了
                if i < length:
                    break
                for word in dic[length]:
                    #同一位置得到的结果是一样的，所以可以直接break
                    if s[i-length:i] == word:
                        dp[i] = dp[i] or dp[i-length]
                        break
        return dp[-1]