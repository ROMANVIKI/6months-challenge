from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for char in matrix[i]:
                if char == target:
                    return True
        return False


sol = Solution()
print(sol.searchMatrix(matrix=[[1], [3]], target=1))
print(
    sol.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )
)
print(
    sol.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    )
)
