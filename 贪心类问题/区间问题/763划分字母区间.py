class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        #和56合并区间类似
        dic = {}
        m = len(s)
        #先记录每个字母起始和结束的位置
        for i in range(m):
            if s[i] not in dic:
                dic[s[i]] = [i,i]
            else:
                dic[s[i]][1] = i
        #然后转化为一道合并区间的题目
        intervals = sorted(list(dic.values()),key=lambda x:x[0])
        n = len(intervals)
        if n == 1:
            return m
        res = []
        left = intervals[0][0]
        right = intervals[0][1]
        for start,end in intervals[1:]:
            if start < right:
                #更新right
                right = max(end,right)
            else:
                #新开一个区间，计算上一个区间的间隔长度
                res.append(right-left+1)
                left = start
                right = end
        #计算最后一个区间的间隔长度
        res.append(right-left+1)
        return res