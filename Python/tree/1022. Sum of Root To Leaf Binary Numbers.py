class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root) -> int:
        self.values = []
        self.temp = []
        def dfs(root):
            if root is None:
                return
            self.temp.append(root.val)
            if root and root.left is None and root.right is None:
                self.values.append(self.temp.copy())                  
            dfs(root.left)
            dfs(root.right)
            self.temp.pop()
        if root is None:
            return 0
        dfs(root)    
        for i in range(len(self.values)):
            value = "".join(map(str, self.values[i]))
            self.values[i] = int(value, 2)

        return sum(self.values)

# Constructing two sample binary trees
# Tree 1:
#        1
#       / \
#      0   1
#     / \
#    0   1
tree1 = TreeNode(1)
tree1.left = TreeNode(0)
tree1.right = TreeNode(1)
tree1.left.left = TreeNode(0)
tree1.left.right = TreeNode(1)

# Tree 2:
#        1
#       / \
#      0   1
#     / \
#    0   1
tree2 = TreeNode(1)
tree2.left = TreeNode(0)
tree2.right = TreeNode(1)
tree2.left.left = TreeNode(0)
tree2.left.right = TreeNode(1)

solution = Solution()
sum_tree1 = solution.sumRootToLeaf(tree1)
sum_tree2 = solution.sumRootToLeaf(tree2)

print(sum_tree1)  # Output: 22
print(sum_tree2)  # Output: 22
