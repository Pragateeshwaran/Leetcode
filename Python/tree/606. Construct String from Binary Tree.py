# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root):
        def dfs(node):
            if not node:
                return ""
            result = str(node.val)
            
            if node.left or node.right:
                result += "(" + dfs(node.left) + ")"
                
            if node.right:
                result += "(" + dfs(node.right) + ")"
            
            return result
        
        return dfs(root)
# Create a binary tree
#      1
#     / \
#    2   3
#   /
#  4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

# Create a Solution instance
solution = Solution()

# Convert the binary tree to a string
result = solution.tree2str(root)

print(result)