class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        #按照起点升序排序，起点相同的按照终点降序排序
        clips.sort(key=lambda x:(x[0],-x[1]))
        count = 0
        curend,nextend = 0,0
        i=0
        n = len(clips)
        #如果start比nextend还大的话，说明中间有间隔，无法拼成视频
        while i < n and clips[i][0] <= curend:
            #我们会比较所有起点小于 clips[i][1] 的区间，根据贪心策略，它们中终点最大的那个区间就是第二个会被选中的视频
            while i < n and clips[i][0] <= curend:
                nextend = max(nextend,clips[i][1])
                i += 1
            #找到下一个视频，更新 curEnd
            count += 1
            curend = nextend
            if curend >= time:
                return count
        return -1

#虽然代码中有一个嵌套的 while 循环，但这个嵌套 while 循环的时间复杂度是 O(N)。因为当 i 递增到 n 时循环就会结束，所以这段代码只会执行 O(N) 次
#对 clips 数组进行了一次排序，消耗了 O(NlogN) 的时间，所以本算法的总时间复杂度是 O(NlogN)