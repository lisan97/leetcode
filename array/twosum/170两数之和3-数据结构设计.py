class TwoSum(object):
    def __init__(self):
        from collections import defaultdict
        self.freq = defaultdict(int)
        
    def add(self,number):
        self.freq[number] += 1

    def find(self,value):
        for key in self.freq:
            other = value - key
            if other == key and self.freq[key] > 1:
                return True
            elif other != key and other in self.freq:
                return True
            else:
                return False

#查询频繁的场景
class TwoSum(object):
    def __init__(self):
        self.sum = set()
        self.nums = []

    def add(self,number):
        for n in self.nums:
            self.sum.add(n + number)
        self.nums.append(number)

    def find(self,value):
        return value in self.sum