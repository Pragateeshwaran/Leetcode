class Solution:

    #  Manacher's algorithm
    def longestPalindrome(self, s: str) -> str:
        # Transform string to handle even-length palindromes
        T = '#' + '#'.join(s) + '#'
        n = len(T)
        P = [0] * n  # P[i] = radius of palindrome centered at i
        C = R = 0  # Center and Right boundary of current palindrome

        for i in range(n):
            # Mirror of i with respect to C
            mirror = 2 * C - i

            # If i is within the right boundary, initialize P[i]
            if i < R:
                P[i] = min(R - i, P[mirror])

            # Attempt to expand palindrome centered at i
            a, b = i + (1 + P[i]), i - (1 + P[i])
            while a < n and b >= 0 and T[a] == T[b]:
                P[i] += 1
                a += 1
                b -= 1

            # If palindrome centered at i expands past R,
            # adjust center and right boundary
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        start = (center_index - max_len) // 2
        return s[start: start + max_len]
    

val = Solution().longestPalindrome("babad")
print(val)


val = Solution().longestPalindrome("cbbd")
print(val)