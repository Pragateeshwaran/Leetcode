class Solution:
    def searchRange(self, nums, target):
        leftpos, rightpos = -1, -1
        l, r = 0, len(nums)-1
        
        while l <= r:   
            mid = (r+l) // 2
            if nums[mid] == target: 
                while mid-1 >= 0 and nums[mid-1] == target:
                    mid -= 1
                leftpos = mid
                while mid+1 <= len(nums)-1 and nums[mid+1] == target:
                    mid += 1
                rightpos = mid
                         
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return [leftpos, rightpos]

print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))