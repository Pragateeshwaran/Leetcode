# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root, low: int, high: int):
        new_tree = None
        
        def construct(root):
            nonlocal new_tree
            
            def dfs(s_root, value):
                if not s_root:
                    return TreeNode(value)
                if s_root.val > value:
                    s_root.left = dfs(s_root.left, value)
                if s_root.val < value:
                    s_root.right = dfs(s_root.right, value)
                return s_root
            
            if not root:
                return
            
            if root.val in range(low, high+1):   
                if not new_tree:
                    new_tree = TreeNode(root.val)   
                else:
                    new_tree = dfs(new_tree, root.val)
                    
            construct(root.left)
            construct(root.right)              
        
        construct(root)
        return new_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root, low: int, high: int):
        def fun(root):
            if root is None: return
            if root.val<low: return fun(root.right)
            if root.val>high: return fun(root.left)
            root.left=fun(root.left)
            root.right=fun(root.right)
            return root
        return fun(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root, low: int, high: int):
        new_tree = None
        def construct(root):
            nonlocal new_tree
            def dfs(s_root, value):
                nonlocal new_tree
                if not s_root:
                    return TreeNode(value)
                if s_root.val > value:
                    s_root.left = dfs(s_root.left, value)
                if s_root.val < value:
                    s_root.right = dfs(s_root.right, value)
                return s_root
            if not root:return
            if root.val in range(low, high+1):   
                if not new_tree:
                    new_tree = TreeNode(root.val)   
                else:
                    new_Tree = dfs(new_tree, root.val)
            construct(root.left)
            construct(root.right)              
        construct(root)
        return new_tree

                        