import heapq, math
class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        res = 0
        nums = [-num for num in nums]  
        heapq.heapify(nums)
        
        for _ in range(k):
            element = -heapq.heappop(nums) 
            res += element
            heapq.heappush(nums, -math.ceil(element/3))  
        
        return res
    
print(Solution().maxKelements(nums = [10,10,10,10,10], k = 5))