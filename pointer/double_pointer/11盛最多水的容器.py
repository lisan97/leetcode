class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            #[i, j] 之间的矩形面积
            area = min(height[i],height[j]) * (j-i)
            res = max(area,res)
            #双指针技巧，移动较低的一边,因为移动较低的那一边，那条边可能会变高，使得矩形的高度变大，进而就「有可能」使得矩形在长度减小的情况下的面积变大
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res