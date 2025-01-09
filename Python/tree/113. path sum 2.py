class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int):
        result = []
        path = []

        def dfs(node, path_sum, path):
            if node is None:
                return

            path_sum += node.val
            path.append(node.val)

            if path_sum == targetSum and node.left is None and node.right is None:
                result.append(path[:])

            dfs(node.left, path_sum, path)
            dfs(node.right, path_sum, path)
            path.pop()

        dfs(root, 0, path)
        return result

# Constructing a sample binary tree
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \    / \
#  7    2  5   1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

targetSum = 22

solution = Solution()
print(solution.pathSum(root, targetSum))  # Output: [[5, 4, 11, 2], [5, 8, 4, 5]]
