
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> str:
        def dfs(node, path_sum):
            if node is None:
                return False
            
            path_sum += node.val
            if path_sum == targetSum and node.left is None and node.right is None:
                return True
            
            return dfs(node.left, path_sum) or dfs(node.right, path_sum)
        
        return dfs(root, 0)
# Constructing a sample binary tree
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \      \
#  7    2      1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

targetSum = 22

solution = Solution()
print(solution.hasPathSum(root, targetSum))  # Output: True
