class Solution(object):
    def minMeetingRooms(self,meetings):
        n = len(meetings)
        if n == 1:
            return 1
        start = []
        end = []
        #把左端点和右端点单独拿出来
        for meeting in meetings:
            start.append(meeting[0])
            end.append(meeting[1])
        start.sort()
        end.sort()
        i,j,count,res = 0,0,0,0
        while i < n and j < n:
            if start[i] < end[j]:
                #扫描到一个起点
                count += 1
                i += 1
            else:
                #扫描到一个终点
                count -= 1
                j += 1
            res = max(res,count)
        return res


if __name__ == '__main__':
    meetings = [[0, 30], [5, 10], [15, 20]]
    print(Solution().minMeetingRooms(meetings))