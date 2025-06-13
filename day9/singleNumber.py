from typing import List


# my solution O(n2)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        for char in count_dict:
            if count_dict[char] == 1:
                return char


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


sol = Solution()
print(sol.singleNumber(nums=[4, 1, 2, 1, 2]))
print(sol.singleNumber(nums=[1]))
