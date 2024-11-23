class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        
        return merged

# Constructing two sample binary trees
# Tree 1:
#        1
#       / \
#      3   2
#     /
#    5
tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(5)

# Tree 2:
#        2
#       / \
#      1   3
#       \
#        4
tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)

solution = Solution()
merged_tree = solution.mergeTrees(tree1, tree2)

# Printing the merged tree's values in an inorder traversal
def inorder_traversal(node):
    if node:
        print(node.val, end=" ")
        inorder_traversal(node.left)
        inorder_traversal(node.right)

inorder_traversal(merged_tree)  # Output: 3 4 5 4 5
