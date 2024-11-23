# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root) -> int:
        def inOrderTraversal(node):
            nonlocal prev_value, min_diff
            if not node:
                return
            
            # Recursively traverse the left subtree
            inOrderTraversal(node.left)
            
            # Calculate the current difference and update min_diff if necessary
            if prev_value is not None:
                current_diff = abs(node.val - prev_value)
                min_diff = min(min_diff, current_diff)
            
            # Update prev_value
            prev_value = node.val
            
            # Recursively traverse the right subtree
            inOrderTraversal(node.right)
        
        prev_value = None
        min_diff = float('inf')  # Initialize min_diff to positive infinity
        inOrderTraversal(root)
        
        return min_diff
    
#       4
#      / \
#     2   6
#    / \
#   1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(Solution().minDiffInBST(root))