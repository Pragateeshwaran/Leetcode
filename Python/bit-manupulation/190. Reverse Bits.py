# class Solution:
#     def reverseBits(self, n: int) -> int:
#         result = 0
#         for i in range(32):
#             # Get the least significant bit of `n`
#             bit = n & 1
#             print(bit)
#             # Shift `result` to the left to make space for the new bit
#             result = (result << 1) | bit
#             # Shift `n` to the right to process the next bit
#             n >>= 1
#         return result

# # Example usage
# if __name__ == "__main__":
#     solution = Solution()
#     n = 43261596  # Input number
#     result = solution.reverseBits(n)
#     print(f"Reversed bits: {result}")  # Output: 964176192
# # 00000010100101000001111010011100


print(2&1)