"""
 Input: intervals = [[0,30],[5,10],[15,20]]
                     s1  e1  s2 e2  s3   e3
                     
  sort(intervals) 
  for i in range(len(intervals)):
    # if e1 > s2, then false 
    if intervals[i][1] > intervals[i+1][0]:
       rturn False
    
  # e1 < s2
  return True

"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
        