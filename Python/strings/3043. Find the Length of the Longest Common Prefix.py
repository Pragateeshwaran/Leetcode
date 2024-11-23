class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        map = {}
        for vals in arr1:
            char = str(vals)
            string = ''
            for c in char:
                string += c
                map[string] = map.get(string, 0) + 1
        
        print(map)
        maxi = 0
        for i in arr2:
            char = str(i)
            string = ''
            for c in char:
                string += c
                if string in map:
                    maxi = max(maxi, len(string))
            
        return maxi

print(Solution().longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]))