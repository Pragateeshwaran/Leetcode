class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_c = close_c = 0
        for c in s:
            if c == '(':
                open_c += 1  # Track unmatched opening parenthesis
            elif c == ')' and open_c > 0:
                open_c -= 1  # Match with an open parenthesis
            else:
                close_c += 1  # Track unmatched closing parenthesis
        return open_c + close_c  # Total unmatched parentheses

print(Solution().minAddToMakeValid('(()))'))