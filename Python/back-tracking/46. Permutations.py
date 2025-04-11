from typing import List

class Solution:
    def helper(self, nums: List[int], used: List[bool], sub: List[int], res: List[List[int]]):
        if len(sub) == len(nums):  # Base case: A valid permutation is found
            res.append(sub[:])  # Append a copy of sub to res
            return
        
        for i in range(len(nums)):
            if not used[i]:  # If nums[i] is not used in the current path
                used[i] = True
                sub.append(nums[i])
                self.helper(nums, used, sub, res)  # Recursive call
                sub.pop()  # Backtrack
                used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)  # Boolean list to track used elements
        res = []
        self.helper(nums, used, [], res)
        return res

# Testing the function
nums = [1, 2, 3]
obj = Solution()
res = obj.permute(nums)

print("Permutations:")
for perm in res:
    print(perm)

