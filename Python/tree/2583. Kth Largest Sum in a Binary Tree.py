# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example usage:
root = TreeNode(5)  # Root node
root.left = TreeNode(3)  # Left child of root
root.right = TreeNode(8)  # Right child of root
root.left.left = TreeNode(1)  # Left child of root.left
root.left.right = TreeNode(4)  # Right child of root.left
root.right.left = TreeNode(7)  # Left child of root.right
root.right.right = TreeNode(9)  # Right child of root.right



class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        if not root:
            return root
        q = [root]
        level_sums = []
        while q:
            nodes_len = len(q)
            sums = 0
            for _ in range(nodes_len):
                node = q.pop(0)
                print(node.val)
                sums += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            print("--")

            level_sums.append(sums)
        print(level_sums)
        return sorted(level_sums)[-k] if k <= len(level_sums) else -1

# Now you can use the kthLargestLevelSum function to find the k-th largest level sum.
solution = Solution()
k = 2
print("K-th largest level sum:", solution.kthLargestLevelSum(root, k))