# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root, val: int):
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node

# Create the nodes
node4 = TreeNode(4)
node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2)

# Set the left and right children
node4.left = node1
node4.right = node3
node3.right = node2

# The tree is now structured as: [4, 1, 3, None, None, 2]
# where None indicates an empty child (null in the tree structure).
