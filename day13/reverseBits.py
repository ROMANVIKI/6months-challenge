# class Solution:
#     def reverseBits(self, n: int) -> int:
#         count = 0
#         n = str(n)
#         n = n[::-1]
#         for i in range(len(n)):
#             count += 2**i
#
#         return count


# class Solution:
#     def reverseBits(self, n: int) -> int:
#         result = 0
#         for i in range(32):
#             bit = n & 1  # Get last bit
#             result = (result << 1) | bit  # Shift result and add bit
#             n >>= 1  # Shift n right to get next bit
#         return result


class Solution:
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


s = Solution()
print(s.reverseBits(n=11111111111111111111111111111101))
print(s.reverseBits(n=110))
# print(s.reverseBits(n=00000010100101000001111010011100))
