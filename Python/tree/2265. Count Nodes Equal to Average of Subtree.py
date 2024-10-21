class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        count = 0

        def dfs(node = root):
            if node is None:
                return 0, 0
            
            val = node.val

            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)

            currSum, currCount = (
                val + leftSum + rightSum,
                1 + leftCount + rightCount
            )

            if currSum // currCount == val:
                nonlocal count
                count += 1
            
            return currSum, currCount
        
        dfs()
        return count



# Create the binary tree
#         5
#        / \
#       3   8
#      /   / \
#     2   7   9

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
solution = Solution()
result = solution.averageOfSubtree(root)
print(result)  # This will print the count of subtrees where the average matches the root value.
