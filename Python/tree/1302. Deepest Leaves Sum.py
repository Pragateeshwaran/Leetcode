class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root) -> int:
        self.result = 0
        self.depth  = 0
        def dfs(root, level):
            if root is None:
                return
            if level > self.depth:
                self.depth = level
                self.result = root.val
            elif level == self.depth:
                print(root.val)
                self.result += root.val
                print("==========>",self.result)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return self.result
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
print(Solution().deepestLeavesSum(root))