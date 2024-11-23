class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(root1,root2):
            if root1 is None or root2 is None:
                return 
            if root1 == target:
                return root2
            
            return (dfs(root1.left,root2.left) 
        or dfs(root1.right,root2.right))

        return dfs(original,cloned)
    


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         def dfs(root1, root2):
#             if not root1:
#                 return None
            
#             if root1 == target:
#                 return root2
            
#             left_result = dfs(root1.left, root2.left)
#             if left_result:
#                 return left_result
            
#             right_result = dfs(root1.right, root2.right)
#             if right_result:
#                 return right_result
            
#             return None

#         return dfs(original, cloned)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        nodes = [(original, cloned)]
        while nodes:
            
            root1, root2 = nodes.pop(0)
            if root1 == target:
                return root2 
            
            if root1.left:
                nodes.append((root1.left, root2.left))
            
            if root1.right:
                nodes.append((root1.right, root2.right))

        return None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        def dfs(root1: TreeNode, root2: TreeNode) -> TreeNode:
            if root1 is None:
                return None
            if root1 == target:
                return root2
            return dfs(root1.left, root2.left) or dfs(root1.right, root2.right)

        return dfs(original, cloned)
    



    
#             1
#     2                    3
# 4           5       6       7

# Create the original tree
original = TreeNode(1)
original.left = TreeNode(2)
original.right = TreeNode(3)
original.left.left = TreeNode(4)
original.left.right = TreeNode(5)
original.right.left = TreeNode(6)
original.right.right = TreeNode(7)

# Create the cloned tree with the same structure
cloned = TreeNode(1)
cloned.left = TreeNode(2)
cloned.right = TreeNode(3)
cloned.left.left = TreeNode(4)
cloned.left.right = TreeNode(5)
cloned.right.left = TreeNode(6)
cloned.right.right = TreeNode(7)

# Define the target node you want to find in the cloned tree
target = original.left.right  # For example, searching for node with value 5

# Now, you can call the getTargetCopy method to find the corresponding node in the cloned tree.
solution = Solution()
result = solution.getTargetCopy(original, cloned, target)
print(result.val)  # This will print the value of the corresponding node in the cloned tree.
