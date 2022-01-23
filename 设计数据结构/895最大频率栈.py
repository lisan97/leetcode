from collections import defaultdict
class FreqStack(object):

    def __init__(self):
        #记录 FreqStack 中每个 val 对应的出现频率，后文就称为 VF 表
        self.val2freq={}
        #记录频率 freq 对应的 val 列表，后文就称为 FV 表
        self.freq2val=defaultdict(list)
        #记录 FreqStack 中元素的最大频率
        self.maxfreq=0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        #修改 VF 表：val 对应的 freq 加一
        freq = self.val2freq.get(val,0) + 1
        self.val2freq[val] = freq
        #修改 FV 表：在 freq 对应的列表加上 val
        self.freq2val[freq].append(val)
        #更新 maxFreq
        self.maxfreq = max(self.maxfreq,freq)

    def pop(self):
        """
        :rtype: int
        """
        #修改 FV 表：pop 出一个 maxFreq 对应的元素 v
        val = self.freq2val[self.maxfreq].pop()
        #修改 VF 表：v 对应的 freq 减一
        self.val2freq[val] -= 1
        #如果 maxFreq 对应的元素空了，更新 maxFreq
        if not self.freq2val[self.maxfreq]:
            self.maxfreq -= 1
        return val