from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        bin = "{0:8b}".format(n)
        for b in bin:
            if b == "1":
                count += 1
        return count


s = Solution()
print(s.hammingWeight(n=2147483645))
