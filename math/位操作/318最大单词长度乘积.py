class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #如果可以将判断两个单词是否有公共字母的时间复杂度降低到 O(1)，则可以将总时间复杂度降低到 O(n^2)。
        #由于单词只包含小写字母，共有 2626 个小写字母，因此可以使用位掩码的最低 2626 位分别表示每个字母是否在这个单词中出现
        masks = []
        for word in words:
            masks.append(reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0))
        max_length = 0
        for x,y in product(zip(masks,words),repeat=2):
            if x[0] & y[0] == 0:
                max_length = max(max_length,len(x[1])*len(y[1]))
        return max_length