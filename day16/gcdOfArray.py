from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        min = nums[0]
        max = nums[-1]

        def gcd(max, min):
            while min:
                max, min = min, max % min
            return max

        return gcd(min, max)


sol = Solution()
print(sol.findGCD(nums=[2, 5, 6, 9, 10]))
print(sol.findGCD(nums=[3, 3]))
print(sol.findGCD(nums=[7, 5, 6, 8, 3]))
