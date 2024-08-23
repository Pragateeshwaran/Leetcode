from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def _flatten(node):
            if not node:
                return None
            left_tail = _flatten(node.left)
            right_tail = _flatten(node.right)
            print(node.val)
            
            if node.left:
                original_right = node.right
                node.right = node.left
                node.left = None
                current = node.right
                while current.right:
                    current = current.right
                current.right = original_right
            return right_tail if right_tail else (left_tail if left_tail else node)

        _flatten(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

# Example tree structure:
#         1
#       /   \
#      2     5
#     / \     \
#    3   4     6

# Flattening the tree
solution = Solution()
solution.flatten(root)

# After flattening, the tree will be modified to:
# 1 - 2 - 3 - 4 - 5 - 6

while root:
    print(root.val)
    root = root.right