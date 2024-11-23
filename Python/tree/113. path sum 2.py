# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def pathSum(self, root, targetSum: int):
#         result = []
#         path = []

#         def dfs(node, path_sum, path):
#             if node is None:
#                 return

#             path_sum += node.val
#             path.append(node.val)

#             if path_sum == targetSum and node.left is None and node.right is None:
#                 result.append(path[:])

#             dfs(node.left, path_sum, path)
#             dfs(node.right, path_sum, path)
#             path.pop()

#         dfs(root, 0, path)
#         return result

# # Constructing a sample binary tree
# #        5
# #       / \
# #      4   8
# #     /   / \
# #    11  13  4
# #   /  \    / \
# #  7    2  5   1

# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
# root.left.left = TreeNode(11)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)

# targetSum = 22

# solution = Solution()
# print(solution.pathSum(root, targetSum))  # Output: [[5, 4, 11, 2], [5, 8, 4, 5]]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_binary(root):
    if root and root.left is None and root.right is None:
        return True

    if root.val > root.left.val and root.val < root.right.val:
        a = True
    else:
        a = False
    return a and is_binary(root.left) and is_binary(root.right)

root = TreeNode(11)              # Root node with value 1
root.left = TreeNode(6)         # Left child of the root with value 2
root.right = TreeNode(13)        # Right child of the root with value 3
root.left.left = TreeNode(5)    # Left child of node 2 with value 4
root.left.left.left = TreeNode(1)    # Left child of node 2 with value 4
root.left.right = TreeNode(7)   # Right child of node 2 with value 5
root.right.left = TreeNode(12)   # Left child of node 3 with value 6
root.right.right = TreeNode(15)  # Right child of node 3 with value 7
print(is_binary(root))
