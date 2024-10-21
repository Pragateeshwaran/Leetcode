
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: [TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False
        
        queue = [(root, None, 0)]
        x_info = None
        y_info = None
        
        while queue:
            node, parent, depth = queue.pop(0)
            
            if node.val == x:
                x_info = (parent, depth)
            elif node.val == y:
                y_info = (parent, depth)

            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
        
        if x_info and y_info and x_info[0] != y_info[0] and x_info[1] == y_info[1]:
            return True
        else:
            return False

            

def isCousins(root, x, y):
    def dfs(node, parent, depth, target):
        if not node:
            return None
        
        if node.val == target:
            return (parent, depth)
        
        left_result = dfs(node.left, node, depth + 1, target)
        if left_result:
            return left_result
        
        return dfs(node.right, node, depth + 1, target)
    
    x_info = dfs(root, None, 0, x)
    y_info = dfs(root, None, 0, y)
    
    if x_info[0] != y_info[0] and x_info[1] == y_info[1]:
        return True
    else:
        return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

x = 5
y = 6

result = isCousins(root, x, y)
print(result) 

