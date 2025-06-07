from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child


sol = Solution()
print(sol.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(sol.findContentChildren(g=[1, 2], s=[1, 2, 3]))
