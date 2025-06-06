class Solution:
    def removeDuplicates(self, nums):
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1

        return i, nums


sol = Solution()
print(sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
