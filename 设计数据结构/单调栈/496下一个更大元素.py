class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #用字典记录每个num的next great number
        res = {}
        stack = []
        #倒着入栈，其实是正着出栈
        for i in range(len(nums2)-1,-1,-1):
            #把两个「个子高」元素之间的元素排除，前面挡着个「更高」的元素，所以他们不可能被作为后续进来的元素的 Next Great Number 了
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            res[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        return [res[num] for num in nums1]