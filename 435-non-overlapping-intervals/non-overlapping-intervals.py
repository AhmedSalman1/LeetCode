class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_end = end
            else:
                res += 1
                prev_end = min(prev_end, end)
        return res