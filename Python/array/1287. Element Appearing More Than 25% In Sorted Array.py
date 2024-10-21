class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        threshold = len(arr) // 4
    
        for i in range(len(arr)):
            if arr[i] == arr[i + threshold]:
                return arr[i]
        
        return -1  
print(Solution().findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))
print(Solution().findSpecialInteger(arr = [1,1]))