from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return 1 
        def dfs(root1, root2):
            if not root1 and not root2:
                return 1
            if (not root1 and root2) or (root1 and not root2):
                return 0 
            
            return root1.val == root2.val and dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        return dfs(p, q)

# Create two identical trees
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

solution = Solution()
print(solution.isSameTree(p, q))  # Output: True
