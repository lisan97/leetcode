class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #每当向右移动时，把窗口左端的值从队列左端剔除，把队列右边小于窗口右端的值全部剔除。
        #这样双端队列的最左端永远是当前窗口内的最大值。--单调栈的一种延申
        from collections import deque
        q = deque()
        n = len(nums)
        res = []
        for i in range(n):
            # 先填满窗口的前 k - 1
            if i < k-1:
                # 将队列尾部小于当前数的元素都删除
                while q and q[-1] < nums[i]:
                    q.pop()
                q.append(nums[i])
            else:
                while q and q[-1] < nums[i]:
                    q.pop()
                q.append(nums[i])
                # 队头的元素肯定是最大的
                res.append(q[0])
                # 要判断队头的数是否==nums[i-k+1]，因为我们想删除的队头元素 可能之前就pop掉了，已经不存在了，所以这时候就不用删除了
                if q[0] == nums[i-k+1]:
                    q.popleft()
        return res