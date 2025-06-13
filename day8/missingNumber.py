from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


sol = Solution()
print(sol.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
