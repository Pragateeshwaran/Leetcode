class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        if not preorder and not inorder:
            return 
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

# Preorder and inorder traversal sequences
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

solution = Solution()
root = solution.buildTree(preorder, inorder)

# Printing the constructed tree using an inorder traversal
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

inorder_traversal(root)  # Output: 9 3 15 20 7
