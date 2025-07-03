from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1

        return n - count, intervals


sol = Solution()
# print(sol.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]))
# print(sol.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
# print(sol.eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]))
print(sol.eraseOverlapIntervals(intervals=[[1, 100], [11, 22], [1, 11], [2, 12]]))
