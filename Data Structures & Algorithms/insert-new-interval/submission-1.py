class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        unseen = []
        for itv in intervals:
            if itv[1] < newInterval[0]:
                res.append(itv)
            else:
                unseen.append(itv)
        
        for itv in unseen:
            if itv[0] < newInterval[0]:
                newInterval[0] = itv[0]
            if itv[1] > newInterval[1] and itv[0] <= newInterval[1]:
                newInterval[1] = itv[1]
        res.append(newInterval)

        for itv in unseen:
            if itv[0] > newInterval[1]:
                res.append(itv)
        return res
        
