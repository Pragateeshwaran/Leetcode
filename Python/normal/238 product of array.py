class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        postfix = 1
        for i in range(n-1,-1,-1):
            res[i]  *= postfix
            postfix *= nums[i]
        return res

print(Solution().productExceptSelf([1,2,3,4]))