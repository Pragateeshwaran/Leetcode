from typing import List
class Solution:
    def combinationSumHelper(self, candidates: List[int], target: int, res: List[List[int]], sub: List[int], index: int):
        if target == 0:
            res.append(sub[:])  # Add a copy of the valid combination
            return 
        if target<0:
            return
        sub.append(candidates[index])
        self.combinationSumHelper(candidates, target-candidates[index], res, sub, index)
        sub.pop()
        if index + 1 < len(candidates):
            self.combinationSumHelper(candidates, target, res, sub, index+1)
        return res 

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.combinationSumHelper(candidates, target, res, [], 0)
        return res
# class Solution:
#     def combinationSumHelper(self, candidates: List[int], target: int, res: List[List[int]], sub: List[int], index: int):
#         if target == 0:
#             res.append(sub[:])  # Add a copy of the valid combination
#             return
        
#         for i in range(index, len(candidates)):
#             sub.append(candidates[i])
            
#             if target - candidates[i] < 0:  # If sum exceeds target, backtrack
#                 sub.pop()
#                 continue
            
#             self.combinationSumHelper(candidates, target - candidates[i], res, sub, i)  # Recursive call
#             sub.pop()  # Backtrack

#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         self.combinationSumHelper(candidates, target, res, [], 0)
#         return res

# Testing the function
candidates = [2, 3, 6, 7]
target = 7
obj = Solution()

res = obj.combinationSum(candidates, target)

print("Combinations:")
for comb in res:
    print(comb)
