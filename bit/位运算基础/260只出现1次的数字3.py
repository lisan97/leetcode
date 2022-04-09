class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #还是先循环做异或运算，最终的结果就只剩下x1和x2的异或和x
        #x & -x 取出 x 的二进制表示中最低位那个 1， 意味着两答案的第 k 位二进制表示不同。
        #对 nums 进行遍历，对第 k 位分别为 0 和 1 的元素分别求异或和
        total = 0
        for num in nums:
            total ^= num
        k = total & (-total)
        type1,type2=0,0
        for num in nums:
            if k & num:
                type1 ^= num
            else:
                type2 ^= num
        return [type1,type2]