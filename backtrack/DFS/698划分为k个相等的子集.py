#以数字的视角,每个数字都要选择进入到 k 个桶中的某一个。
# n 个数字，每个数字有 k 个桶可供选择，O(k^n)会超时
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        # 就可以减少递归调用的次数，从大的数字开始遍历，更快达到剪枝条件
        nums.sort(reverse=True)
        target = total / k
        # k 个桶（集合），记录每个桶装的数字之和
        track = [0] * k
        return self.backtrack(nums, track, k, 0, target)

    def backtrack(self, nums, track, k, index, target):
        # index=len(nums)说明遍历nums结束，检查所有桶的数字之和是否都是 target
        if index == len(nums):
            for item in track:
                if item != target:
                    return False
            return True
        # 穷举 nums[index] 可能装入的桶
        for j in range(k):
            # 剪枝，桶装装满了
            if track[j] + nums[index] > target:
                continue
            # 将 nums[index] 装入 bucket[i]
            track[j] += nums[index]
            # 递归穷举下一个数字的选择
            if self.backtrack(nums, track, k, index + 1, target):
                return True
            # 撤销选择
            track[j] -= nums[index]
        return False

#以桶的视角
#每个桶要遍历 n 个数字，对每个数字有「装入」或「不装入」两种选择，所以组合的结果有 2^n 种；而我们有 k 个桶，所以总的时间复杂度为 O(k*2^n)
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        self.memo = {}  # 在装满一个桶时记录当前 used 的状态
        used = [False] * len(nums)  # 记录nums[i] 已经被装入别的桶中
        target = total / k
        return self.backtrack(k, 0, nums, 0, used, target)

    def backtrack(self, k, bucket, nums, start, used, target):
        # base case
        if k == 0:
            # 所有桶都被装满了，而且 nums 一定全部用完了
            return True

        if bucket == target:
            # 装满了当前桶，递归穷举下一个桶的选择,让下一个桶从 nums[0] 开始选数字
            res = self.backtrack(k - 1, 0, nums, 0, used, target)
            self.memo[tuple(used)] = res
            return res

        if tuple(used) in self.memo:
            return self.memo[tuple(used)]

        for i in range(start, len(nums)):
            # 剪枝,判断第 i 位是否是 1，若为1则nums[i] 已经被装入别的桶中
            if used[i]:
                continue
            if bucket + nums[i] > target:
                continue
            # 做选择，将 nums[i] 装入当前桶中
            used[i] = True
            bucket += nums[i]
            # 递归穷举下一个数字是否装入当前桶
            if self.backtrack(k, bucket, nums, i + 1, used, target):
                return True
            # 撤销选择
            used[i] = False
            bucket -= nums[i]
        return False
#每次递归都要把 used 列表转化成元组，这对于编程语言来说也是一个不小的消耗，所以我们还可以进一步优化
#注意题目给的数据规模 nums.length <= 16，也就是说 used 数组最多也不会超过 16，那么我们完全可以用「位图」的技巧，用一个 int 类型的 used 变量来替代 used 数组
#可以用整数 used 的第 i 位（(used >> i) & 1）的 1/0 来表示 used[i] 的 true/false。这样还节约了空间
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        self.memo = {}  # 在装满一个桶时记录当前 used 的状态
        used = 0  # 使用位图技巧
        target = total / k
        return self.backtrack(k, 0, nums, 0, used, target)

    def backtrack(self, k, bucket, nums, start, used, target):
        # base case
        if k == 0:
            # 所有桶都被装满了，而且 nums 一定全部用完了
            return True

        if bucket == target:
            # 装满了当前桶，递归穷举下一个桶的选择,让下一个桶从 nums[0] 开始选数字
            res = self.backtrack(k - 1, 0, nums, 0, used, target)
            self.memo[used] = res
            return res

        if used in self.memo:
            return self.memo[used]

        for i in range(start, len(nums)):
            # 剪枝,判断第 i 位是否是 1，若为1则nums[i] 已经被装入别的桶中
            if ((used >> i) & 1) == 1:
                continue
            if bucket + nums[i] > target:
                continue
            # 做选择
            used |= 1 << i  # 将第 i 位置为 1
            bucket += nums[i]
            # 递归穷举下一个数字是否装入当前桶
            if self.backtrack(k, bucket, nums, i + 1, used, target):
                return True
            # 撤销选择
            used ^= 1 << i  # 使用异或运算将第 i 位恢复 0
            bucket -= nums[i]
        return False