class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        #max(len(tasks), (maxexc-1)*(n+1)+maxcount)
        from collections import defaultdict
        dic = defaultdict(int)
        for task in tasks:
            dic[task] += 1
        sort_dic = sorted([(k,v) for k,v in dic.items()],key=lambda x:-x[1])
        maxexc = sort_dic[0][1]
        res = (maxexc-1) * (n+1)
        for i in range(len(sort_dic)):
            if sort_dic[i][1] == maxexc:
                res += 1
            else:
                break
        return max(res,len(tasks))