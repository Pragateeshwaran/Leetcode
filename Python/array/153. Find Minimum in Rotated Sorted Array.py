class Solution:
    def findMin(self,nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = ( left + right ) // 2

            # Check if the middle element is greater than the rightmost element
            if nums[mid] > nums[right]:
                left = mid + 1
            # Check if the middle element is less than the rightmost element
            elif nums[mid] < nums[right]:
                right = mid
            # If they are equal, we can't decide which half to discard, so decrement right
            else:
                right -= 1

        return nums[left]
    
print(Solution().findMin(nums = [4,5,6,7,0,1,2]))
print(Solution().findMin(nums = [3,4,5,1,2]))
# 11 12 13 14 0 1