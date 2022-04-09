class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        #base = 1337
        if not b:
            return 1
        last = b.pop()
        part1 = self.mypow(a, last)
        part2 = self.mypow(self.superPow(a, b), 10)
        return (part1 * part2) % 1337

    def mypow(self, a, k):
        if k == 0:
            return 1
        a %= 1337

        if k % 2 == 1:
            return (a * self.mypow(a, k - 1)) % 1337
        else:
            sub = self.mypow(a, k / 2)
            return (sub ** 2) % 1337