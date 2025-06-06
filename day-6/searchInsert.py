class Solution:
    def searchInsert(self, nums, target):
        ind = 0
        while ind <= len(nums) - 1:
            if nums[ind] == target:
                return ind
            elif nums[ind] > target:
                return ind
            ind += 1
        return len(nums)


sol = Solution()
print(sol.searchInsert(nums=[1, 3, 5, 6], target=5))
print(sol.searchInsert(nums=[1, 3, 5, 6], target=2))
print(sol.searchInsert(nums=[1, 3, 5, 6], target=7))
