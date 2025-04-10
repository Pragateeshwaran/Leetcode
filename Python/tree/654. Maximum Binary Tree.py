# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        
        return root

# Given input
nums = [3, 2, 1, 6, 0, 5]

# Creating the Solution instance
solution = Solution()

# Constructing the maximum binary tree
root = solution.constructMaximumBinaryTree(nums)

# Now 'root' contains the root node of the maximum binary tree