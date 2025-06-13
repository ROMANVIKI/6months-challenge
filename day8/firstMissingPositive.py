from typing import List


class Solution:  ## ---- not accepted
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1, len(nums) + 1):
            if i in nums:
                continue
            else:
                return i


sol = Solution()
# print(sol.firstMissingPositive(nums=[7, 8, 9, 11, 12]))
print(sol.firstMissingPositive(nums=[1, 2, 0]))
