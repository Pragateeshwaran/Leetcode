class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        term_i = -1  # This will store the index of the largest digit found
        max_i = -1   # This will store the index of the digit to swap
        min_i = -1   # This will store the index of the digit being swapped with max_i
        max_term = -1

        # Iterate through the digits from right to left
        for i in range(len(num) - 1, -1, -1):
            digit = int(num[i])
            if digit > max_term:
                max_term = digit
                term_i = i  # Update the position of the largest digit found
            elif digit < max_term:
                # We found a smaller digit before a larger one, so update indices for swap
                max_i, min_i = term_i, i

        # Perform the swap if valid indices were found
        if max_i != -1 and min_i != -1:
            num[max_i], num[min_i] = num[min_i], num[max_i]  # Correct the swap

        return int("".join(num))  # Convert back to int and return

# Example usage
solution = Solution()
print(solution.maximumSwap(98368))  # Output: 98863
