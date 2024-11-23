# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Creating the binary search tree nodes
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# Example nodes to find the lowest common ancestor
p = root.left  # Node with value 2
q = root.left.right  # Node with value 4

# Solution class with the lowestCommonAncestor method
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode') -> "TreeNode":
            if not root:
                return
            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            elif p.val < root.val and q.val < root.val:
                return dfs(root.left)
            else:
                return root
        return dfs(root)
 
solution = Solution()
# Find and print the lowest common ancestor
lca = solution.lowestCommonAncestor(root, p, q)
print(f"Lowest Common Ancestor of {p.val} and {q.val} is: {lca.val}")
