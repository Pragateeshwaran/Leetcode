# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root):
        def bfs(root):
            if root is None:
                return
            q = [[None, root, 1]]
            node_return = root
            height_return = 0
            while q:
                parent, node, height = q.pop(0)
                if height_return < height and (node.left or node.right):
                    node_return = parent
                height_return = max(height_return, height)
                if node.left:
                    q.append([node, node.left, height+1])
                if node.right:
                    q.append([node, node.right, height+1])

            if node_return.left and node_return.right:
                return node_return
            if node_return.left and not node_return.right:
                return node_return.left
            if node_return.right and not node_return.right:
                return node_return.right
        return bfs(root)
    
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
print(Solution().lcaDeepestLeaves(root))