class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rangeSumBST(self, root, low: int, high: int) -> int:
#         def dfs(node):
#             if node is None:
#                 return 0
            
#             if node.val < low:
#                 return dfs(node.right)
#             elif node.val > high:
#                 return dfs(node.left)
#             else:
#                 return node.val + dfs(node.left) + dfs(node.right)
        
#         return dfs(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        sums = 0
        def bfs(root):
            nonlocal sums
            if root is None:
                return 0
            q = [root]
            while q:
                node = q.pop(0)
                print(q)
                if low <= node.val <= high:
                    print(node.val)
                    sums+= node.val
                if node.right:
                    q.append(node.right) 
                if node.left:
                    q.append(node.left)
        bfs(root)
        return sums

# class Solution:
#     def rangeSumBST(self, root, low: int, high: int) -> int:
#         def dfs(root):
#             if root is None:
#                 return 0
#             c = 0
#             if low <= root.val <= high:
#                 c += root.val
#             c += dfs(root.left)
#             c += dfs(root.right)
#             print(c)
#             return c
#         return dfs(root)

# Constructing a sample binary search tree
#        10
#       /  \
#      5   15
#     / \    \
#    3   7   18

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

low = 7
high = 15

solution = Solution()
range_sum = solution.rangeSumBST(root, low, high)
print(range_sum)  # Output: 32 (10 + 15 + 7)
