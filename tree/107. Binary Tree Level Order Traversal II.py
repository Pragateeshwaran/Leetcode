from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, level):
            if not node:
                return
            
            # Ensure `res` has enough lists for each level
            if len(res) <= level:
                res.append([])

            # Add the current node's value to its corresponding level
            res[level].append(node.val)

            # Traverse left and right children, increasing the level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        # Start DFS from the root at level 0
        dfs(root, 0)

        # Reverse the result to get bottom-up level order
        return res[::-1]

# Example usage:
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
sol = Solution()
print(sol.levelOrderBottom(root))
