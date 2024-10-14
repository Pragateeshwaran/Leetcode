# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

# Constructing the tree
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# Applying the solution
class Solution:
    def connect(self, root):
        def dfs(root):
            if not root:
                return
            if root.left:
                root.left.next = root.right
            if root.right and root.next:
                root.right.next = root.next.left
            dfs(root.left)
            dfs(root.right)
            return root
        return dfs(root)    
   
print(Solution().connect(node1))