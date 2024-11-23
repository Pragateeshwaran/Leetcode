# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         val = []
        
#         def bfs(node):
#             if node is None:
#                 return
#             queue = [node]
#             while queue:
#                 current = queue.pop(0)
#                 val.append(current.val)
#                 if current.left:
#                     queue.append(current.left)
#                 if current.right:
#                     queue.append(current.right)
        
#         bfs(root)
        
#         for i in val:
#             for j in val:
#                 if i != j and i + j == k:
#                     return True
#         return False

class Solution:
    def findTarget(self, root, k: int) -> bool:
        def dfs(root, target, seen):
            if root is None:
                return False
            complement = target - root.val
            if complement in seen:
                return True
            seen.add(root.val)
            return dfs(root.left, target, seen) or dfs(root.right, target, seen)

        seen = set()
        return dfs(root, k, seen)

# Create a simple binary search tree:
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

# Create an instance of the Solution class
solution = Solution()

# Call the minDiffInBST function with the root of the BST
min_diff = solution.findTarget(root,5)
print(min_diff)
