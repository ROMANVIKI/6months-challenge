from typing import List

# wrong solution ------------------------>


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num = ("").join(map(str, b))
        return a ** int(num)


s = Solution()
print(s.superPow(a=1, b=[4, 3, 3, 8, 5, 2]))
print(s.superPow(a=2, b=[3]))
print(s.superPow(a=2, b=[1, 0]))
print(s.superPow(a=2147483647, b=[2, 0, 0]))
