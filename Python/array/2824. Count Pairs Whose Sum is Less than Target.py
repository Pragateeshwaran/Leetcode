class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        # -1 1 1 2 3
        nums.sort()
        n=len(nums)
        count=0
        i=0
        j=n-1
        while(i<n and i<j):
            if nums[i]+nums[j]<target:
                count+=j-i
                i+=1
            elif nums[i]+nums[j]>=target:
                j-=1
            
        return count
print(Solution().countPairs(nums = [-1,1,2,3,1], target = 2))   #----------->3
print(Solution().countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2))   #----------->10