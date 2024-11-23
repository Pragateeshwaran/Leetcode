class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0  # To keep track of the number of paths
        
        def dfs(node, current_sum):
            if not node:
                return
            
            current_sum += node.val
            
            if current_sum == targetSum:
                self.count += 1
            
            # Recurse on left and right subtrees
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            # Explore other paths starting from the parent of the current node
            dfs(node.left, 0)
            dfs(node.right, 0)
        
        dfs(root, 0)
        return self.count

# Creating the binary tree
# Example tree:        10
#                    /    \
#                   5     -3
#                  / \      \
#                 3   2     11
#                / \   \
#               3  -2   1

# Leaf nodes
leaf1 = TreeNode(3)
leaf2 = TreeNode(2)
leaf3 = TreeNode(11)
leaf4 = TreeNode(3)
leaf5 = TreeNode(-2)
leaf6 = TreeNode(1)

# Middle level nodes
middle1 = TreeNode(5, leaf1, leaf2)
middle2 = TreeNode(-3, None, leaf3)
middle3 = TreeNode(3, leaf4, leaf5)

# Root node
root = TreeNode(10, middle1, middle2)
middle1.left = middle3

# Creating the Solution instance
solution = Solution()

# Calculating the number of paths with targetSum = 8
targetSum = 8
result = solution.pathSum(root, targetSum)
print(result)  # Output should be 3
