# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root) -> int:

        
        self.result = 0
        def dfs(root,val):

            if root is None:
                return

            val = val * 10 + root.val
            if root.left is None and not root.right:
                self.result += val               
            dfs(root.left,val)
            dfs(root.right,val)
            

        dfs(root,0)
        return self.result
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().sumNumbers(root))