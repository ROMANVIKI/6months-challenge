from typing import List


class Solution:  # ------ wrong answer ------- #
    def jump(self, nums: List[int]) -> int:
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[-1]:
                return count
            elif nums[i] < nums[i + 1]:
                i += nums[i + 1]
                count += 1
            else:
                count += 1
        return count


sol = Solution()
print(sol.jump(nums=[2, 3, 1, 1, 4]))
print(sol.jump(nums=[2, 3, 0, 1, 4]))
