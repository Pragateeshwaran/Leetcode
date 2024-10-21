class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start: int, seen: set) -> int:
            if start == len(s):
                return len(seen)
            
            max_unique = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                # print(substring)
                if substring not in seen:
                    seen.add(substring)
                    max_unique = max(max_unique, backtrack(end, seen))
                    seen.remove(substring)
                    
            return max_unique
        
        return backtrack(0, set())

soln = Solution()
print(soln.maxUniqueSplit(s = "ababccc"))
print(soln.maxUniqueSplit(s = "aba"))