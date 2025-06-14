class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0


class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        return 1162261467 % n == 0


# The largest power of 3 within signed 32-bit int is 3^19 = 1162261467. Since powers of 3 are closed under multiplication, any true power of 3 will divide 3^19 evenly.


sol = Solution()
print(sol.isPowerOfThree(n=27))
print(sol.isPowerOfThree(n=45))
print(sol.isPowerOfThree(n=-1))
print(sol.isPowerOfThree(n=0))
