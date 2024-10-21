class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        def inOrder(node):
            nonlocal k, result

            if not node or k == 0:
                return

            inOrder(node.left) 
            k -= 1
            if k == 0:
                result = node.val 

            inOrder(node.right) 

        result = None
        inOrder(root) 
        return result


# Create nodes
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# The binary tree looks like this:
#        10
#       /  \
#      5    15
#     / \   / \
#    3   7 12 18
