class Solution:
    def maxLength(self, arr):
        def is_unique(s):
            return len(s) == len(set(s))

        def backtrack(index, current):
            nonlocal max_length
            print(current)
            if is_unique(current):
                max_length = max(max_length, len(current))
            else:
                return
            for i in range(index, len(arr)):
                backtrack(i + 1, current + arr[i])

        max_length = 0
        backtrack(0, '')
        return max_length

# Example usage:
solution = Solution()
# print(solution.maxLength(["un","iq","ue"]))  # Output: 4
print(solution.maxLength(["r","cha","act","ers"]))  # Output: 6
# print(solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]))  # Output: 26
