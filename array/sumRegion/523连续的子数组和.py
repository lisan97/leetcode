class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return False
        dic = {0:0}
        sumarry = [0] * (n+1)
        for i in range(1,n+1):
            sumarry[i] = sumarry[i-1] + nums[i-1]
            dic[sumarry[i]] = i
        maxnum = sumarry[-1]
        could = maxnum // k < n
        for i in range(n-1):
            if could:
                for num in range(0,maxnum+1,k):
                    target = sumarry[i]+num
                    if target in dic and abs(i - dic[target])>1:
                        return True
            else:
                for j in range(i+2,n+1):
                    diff = sumarry[j] - sumarry[i]
                    if not diff % k:
                        return True
        return False

#要使得两者除 k相减为整数，需要满足 sum[j] 和 sum[i−1] 对 k 取余相同
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return False
        sumarry = [0] * (n+1)
        for i in range(1,n+1):
            sumarry[i] = sumarry[i-1] + nums[i-1]
        visited = set()
        for i in range(2,n+1):
            visited.add(sumarry[i-2] % k)
            if sumarry[i] % k in visited:
                return True
        return False