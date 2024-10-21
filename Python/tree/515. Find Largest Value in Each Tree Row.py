# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            level_max = float("-inf")
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)
                level_max = max(level_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_max)

        return res

# Create the tree
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
solution = Solution()
result = solution.largestValues(root)
print(result)  # This will print [1, 3, 9], which are the largest values in each level.
#      1
#     / \
#    3   2
#   / \   \
#  5   3   9
