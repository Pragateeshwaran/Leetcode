class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        res = float('-inf')
        for i in range(len(nums)):
            if i+k > len(nums)-1:
                return res
            val = sum(nums[i:k+i])
            fin_val = val/k
            res = max(fin_val, res)
        return res
print(Solution().findMaxAverage( nums = [1,12,-5,-6,50,3], k = 4))