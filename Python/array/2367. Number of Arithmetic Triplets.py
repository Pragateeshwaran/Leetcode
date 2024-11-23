"""
num[j] - num[i] = diff ---> num[i] + diff = num[j] -----> 1 condition
num[k] - num[j] = diff ---> num[j] + diff = num[k] -----> (diff + num[i] ) + diff ----> 2 diff + num[i]-----> 2 condition
"""
class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] + diff in nums and nums[i] + (2 * diff) in nums: 
                cnt += 1

        return cnt
print(Solution().arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))   # o/p 2
print(Solution().arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))    # o/p 2