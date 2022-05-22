class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        res_dic = defaultdict(list)
        for chars in strs:
            key = self.countchar(chars)
            res_dic[key].append(chars)
        return list(res_dic.values())


    def countchar(self,chars):
        count_dic = [0] * 26
        for c in chars:
            count_dic[ord(c)-ord('a')] += 1
        key = ''
        for i in range(26):
            if count_dic[i] > 0:
                key += chr(ord('a')+i)+str(count_dic[i])
        return key

#用tuple当key，速度快一点，空间复杂度高一些
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        res_dic = defaultdict(list)
        for chars in strs:
            key = self.countchar(chars)
            res_dic[key].append(chars)
        return list(res_dic.values())


    def countchar(self,chars):
        count_dic = [0] * 26
        for c in chars:
            count_dic[ord(c)-ord('a')] += 1
        return tuple(count_dic)