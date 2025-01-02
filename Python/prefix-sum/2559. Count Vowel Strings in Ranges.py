class Solution:
    def is_vowel(self, c: str) -> bool:
        """Check if a character is a vowel."""
        return c in 'aeiou'

    def is_vowel_string(self, s: str) -> bool:
        """Check if a string is a vowel string (starts and ends with vowels)."""
        if not s:  # Handle empty strings
            return False
        return self.is_vowel(s[0]) and self.is_vowel(s[-1])

    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        """Count the number of vowel strings within the range of each query."""
        n = len(words)
        prefix_sum = [0] * (n + 1)

        # Precompute prefix sums based on whether each word is a vowel string
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if self.is_vowel_string(words[i]) else 0)
        print(prefix_sum)
        res = []
        for l, r in queries:
            res.append(prefix_sum[r + 1] - prefix_sum[l])

        return res
# Example inputs
words = ["apple", "banana", "orange", "umbrella", "egg"]
queries = [[0, 2], [1, 4], [0, 4]]

# Create an instance of Solution
solution = Solution()

# Get the results
result = solution.vowelStrings(words, queries)
print(result)  # Output: [2, 3, 3]
