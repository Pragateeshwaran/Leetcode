class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True
            if not (lower < node.val < upper):
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root)

# Constructing a sample binary tree that is a valid BST
#        2
#       / \
#      1   3

root_valid = TreeNode(2)
root_valid.left = TreeNode(1)
root_valid.right = TreeNode(3)

# Constructing a sample binary tree that is not a valid BST
#        5
#       / \
#      1   4
#         / \
#        3   6

root_invalid = TreeNode(5)
root_invalid.left = TreeNode(1)
root_invalid.right = TreeNode(4)
root_invalid.right.left = TreeNode(3)
root_invalid.right.right = TreeNode(6)

solution = Solution()
print(solution.isValidBST(root_valid))    # Output: True (Valid BST)
print(solution.isValidBST(root_invalid))  # Output: False (Not a valid BST)

