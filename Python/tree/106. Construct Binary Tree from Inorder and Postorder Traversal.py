class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]):
        if not inorder or not postorder:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        index = inorder.index(root_val)
        
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        
        return root

# Inorder and postorder traversal sequences
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

solution = Solution()
root = solution.buildTree(inorder, postorder)

# Printing the constructed tree using an inorder traversal
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

inorder_traversal(root)  # Output: 9 3 15 20 7

