class Solution(object):
    def minMeetingRooms(self,meetings):
        if len(meetings) == 1:
            return 1
        meetings.sort(key = lambda x: x[1])
        res = 1
        count = 1
        end = meetings[0][1]
        for meeting in meetings[1:]:
            start = meeting[0]
            

if __name__ == '__main__':
    meetings = [[0, 30], [5, 10], [15, 20]]
    print(Solution().minMeetingRooms(meetings))