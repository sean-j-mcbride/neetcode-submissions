"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end, s, e = [], [], 0, 0
        res = count = 0

        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        
        start.sort(), end.sort()

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
