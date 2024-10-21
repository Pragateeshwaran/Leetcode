# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def allPossibleFBT(self, n: int):
#         dp = {0 : [], 1 : [TreeNode()]}
#         i = 10
#         def backtrack(n):
#             nonlocal i
#             if n in dp:
#                 return dp[n]
#             res = []
#             for l in range(n):                
#                 r = n-l-1
#                 print(f"rr {r}, ll {l} , n {n}")
#                 lefttrees  = backtrack(l)
#                 righttrees =  backtrack(r)
#                 print(f"=======>left tree is {lefttrees}")
#                 print(f"=======>rightt tree is {righttrees}")
#                 for t1 in lefttrees:
#                     for t2 in righttrees:
#                         res.append(TreeNode(i,t1,t2))
#                         i += 1
#             dp[n] = res
#             print("------->",dp)
#             return res
#         return backtrack(n)
# Definition for a binary tree node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.memo = {}  # Initialize the memoization dictionary
    
    def allPossibleFBT(self, n: int):
        if n % 2 == 0:
            return []  # FBT cannot have an even number of nodes
        
        if n == 1:
            return [TreeNode(0)]
        
        if n in self.memo:
            return self.memo[n]
        
        result = []
        for left_count in range(1, n, 2):  # Iterate through odd numbers for left subtree size
            right_count = n - 1 - left_count  # Calculate right subtree size
            left_trees = self.allPossibleFBT(left_count)
            right_trees = self.allPossibleFBT(right_count)
            
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)
        
        self.memo[n] = result
        return result

a = Solution().allPossibleFBT(5)
print("the vale is ",a)
# def bfs(i):
#     q  = [i]
#     while q:
#         vode = q.pop(0)
#         print("--->",vode.val,end = "")
#         if vode.left:
#             q.append(vode.left)
#         if vode.right:
#             q.append(vode.right)
        


# for i in a:
#     bfs(i)
#     print("\n")
