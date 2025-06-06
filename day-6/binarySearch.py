class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            med = (left + right) // 2

            if nums[med] == target:
                return med
            elif nums[med] < target:
                left = med + 1
            else:
                right = med - 1
        return -1


sol = Solution()
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
