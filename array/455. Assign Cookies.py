class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()
        g_index = 0
        s_index = 0
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                g_index += 1
            s_index += 1
        return g_index
    

print(Solution().findContentChildren( g = [1,2,3], s = [1,1]))# 1
print(Solution().findContentChildren(g = [1,2], s = [1,2,3]))# 2

