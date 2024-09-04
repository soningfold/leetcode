#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        merged = []
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end) # end becomes the bigger of the 2 overlapping intervals
            else:
                merged.append([start, end]) # no conflict meaning we can append the current interval created
                start = intervals[i][0] # as we are looking at the next index already, we can just do i
                end = intervals[i][1]

        merged.append([start,end]) # 
        
        return merged
# @lc code=end

