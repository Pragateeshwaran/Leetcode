class Solution:
    def search(self, nums, target: int) -> int:
        start = 0
        end   = len(nums)-1
        mid = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                mid = i+1
                break 

        if target == nums[mid]:
            return mid        
        elif target <= nums[end]:
            start = mid
        else:
            end = mid-1

        while (start <= end):
            mid = (start+end)//2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1

print(Solution().search(
[9,10,11,1,2,3,4,5], 9
))