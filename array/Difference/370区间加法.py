from Difference import Difference
class Solution(object):
    def getModifiedArray(self, length, updates):
        nums = [0] * length
        df = Difference(nums)
        for update in updates:
            i,j,val = update[0],update[1],update[2]
            df.increment(i,j,val)
        return df.result()

if __name__ == '__main__':
    length = 5
    updates = [[1,3,2],[2,4,3],[0,2,-2]]
    s = Solution()
    print(s.getModifiedArray(length,updates))
