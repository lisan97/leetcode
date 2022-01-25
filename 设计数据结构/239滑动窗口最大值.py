from collections import deque


class MonotonicQueue(object):
    def __init__(self):
        self.q = deque()

    def push(self, n):
        # 将前面小于自己的元素都删除
        while self.q and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)

    def max(self):
        # 队头的元素肯定是最大的
        return self.q[0]

    def pop(self, n):
        # 要判断 data.front() == n，是因为我们想删除的队头元素 n 可能已经被「压扁」了，可能已经不存在了，所以这时候就不用删除了
        if n == self.q[0]:
            self.q.popleft()


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        window = MonotonicQueue()
        for i in range(len(nums)):
            if i < k - 1:
                # 先填满窗口的前 k - 1
                window.push(nums[i])
            else:
                # 窗口向前滑动，加入新数字
                window.push(nums[i])
                # 记录当前窗口的最大值
                res.append(window.max())
                # 移出旧数字
                window.pop(nums[i - k + 1])
        return res