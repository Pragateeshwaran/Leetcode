class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = [['' for _ in range(len(s))] for _ in range(numRows)]

        # Populate the matrix with characters from the input string
        row, col, direction = 0, 0, 1
        for char in s:
            res[row][col] = char
            if row == 0:
                direction = 1  # Change direction when reaching the top row
            elif row == numRows - 1:
                direction = -1  # Change direction when reaching the bottom row
            row += direction
            col += 1

        # Combine the characters from the matrix into a single string
        result = ''.join(''.join(row) for row in res)
        return result

# Example usage
solution = Solution()
result = solution.convert("PAYPALISHIRING", 3)
print(result)
