class Solution:
    def leftRightDifference(self, nums:list[int]) -> list[int]:
        left_sum = 0
        right_sum = 0
        res = []

        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            res.append(abs(left_sum-right_sum))
        return res

print(Solution().leftRightDifference(nums = [10,4,8,3]))