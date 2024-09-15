from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        result = Counter(words[0])
        for word in words[1:]:
            result &= Counter(word)
        
        return list(result.elements())

solution = Solution()
print(solution.commonChars(["bella", "label", "roller"]))  # Output: ['e', 'l', 'l']
print(solution.commonChars(["cool", "lock", "cook"]))  # Output: ['c', 'o']