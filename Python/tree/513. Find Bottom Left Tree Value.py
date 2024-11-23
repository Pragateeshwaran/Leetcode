class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root) -> int:

        self.result = (0, 0)  
        def dfs(root, depth):
            if root is None:
                return
            if depth > self.result[0]:
                self.result = (depth, root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return self.result[1]

root = TreeNode(1)              # Root node with value 1
root.left = TreeNode(2)         # Left child of the root with value 2
root.right = TreeNode(3)        # Right child of the root with value 3
root.left.left = TreeNode(4)    # Left child of node 2 with value 4
root.left.left.left = TreeNode(41)    # Left child of node 2 with value 4
root.left.right = TreeNode(5)   # Right child of node 2 with value 5
root.right.left = TreeNode(6)   # Left child of node 3 with value 6
root.right.right = TreeNode(7)  # Right child of node 3 with value 7
print(Solution().findBottomLeftValue(root))