"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


        Input: intervals = [interval(5,8),interval(9,15)]
                                     1               2   
                            len = 2 
                            
        Output: true
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
            
        return True


