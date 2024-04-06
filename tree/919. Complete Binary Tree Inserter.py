from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.deque = deque()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent = self.deque[0]
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.deque.popleft()
        self.deque.append(new_node)
        return parent.val

    def get_root(self):
        return self.root
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# Definition for a binary tree node.
# Create the initial complete binary tree
# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Instantiate the CBTInserter object
cbt_inserter = CBTInserter(root)

# Insert additional nodes
cbt_inserter.insert(6)
cbt_inserter.insert(7)

# Retrieve the root of the modified tree
new_root = cbt_inserter.get_root()

# Print the new tree structure
# The tree should now have the additional nodes inserted while maintaining completeness.
# Example:
#        1
#       / \
#      2   3
#     / \ /
#    4  5 6
#   /
#  7
def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

print_tree(new_root)
