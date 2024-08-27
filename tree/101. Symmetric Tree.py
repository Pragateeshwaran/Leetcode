class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(root_left, root_right):
            if not root_left and not root_right:
                return 1
            if (not root_left and root_right) or (root_left and not root_right):
                return 0
            
            return root_left.val == root_right.val and dfs(root_left.left, root_right.right) and dfs(root_left.right, root_right.left)
        
        if not root:
            return 1
        
        return dfs(root.left, root.right) 
    

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3



# Creating the tree nodes
root = TreeNode(1)                           # Root node
root.left = TreeNode(2)                      # Left child of root
root.right = TreeNode(2)                     # Right child of root
root.left.left = TreeNode(3)                 # Left child of left node
root.left.right = TreeNode(4)                # Right child of left node
root.right.left = TreeNode(4)                # Left child of right node
root.right.right = TreeNode(3)               # Right child of right node

# Creating an instance of the Solution class
solution = Solution()

# Checking if the tree is symmetric
is_symmetric = solution.isSymmetric(root)
print(is_symmetric)
