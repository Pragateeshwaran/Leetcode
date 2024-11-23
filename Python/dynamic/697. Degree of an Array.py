class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        # Step 1: Find the degree of array (max frequency)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        degree = max(count.values())
        
        # Step 2: Use two pointers to find smallest window
        left = 0
        freq = {}
        min_length = len(nums)
        
        # Move right pointer
        for right in range(len(nums)):
            # Add new number to frequency count
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # If we found a window with the degree
            while freq[nums[right]] == degree:
                # Calculate window size
                min_length = min(min_length, right - left + 1)
                
                # Shrink window from left
                freq[nums[left]] -= 1
                left += 1
        
        return min_length

print(Solution().findShortestSubArray(nums = [1,2,2,3,1,4,2]))