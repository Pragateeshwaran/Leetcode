import heapq 
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if not a and not b and not c:
            return ""
        lists = []
        if a:
            heapq.heappush(lists, (-a, "a"))
        if b:
            heapq.heappush(lists, (-b, "b"))
        if c:
            heapq.heappush(lists, (-c, "c"))
        res = ""
        while lists:
            char_len, char = heapq.heappop(lists)
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if lists:
                    char_len2, char2 = heapq.heappop(lists)
                    char_len2 += 1
                    res += char2
                    if char_len2 < 0:
                        heapq.heappush(lists, (char_len2, char2))
                    heapq.heappush(lists, (char_len, char))
            else:
                res += char
                char_len += 1
                if char_len < 0:
                    heapq.heappush(lists, (char_len, char))
        return res
        
print(Solution().longestDiverseString(a = 1, b = 1, c = 7))