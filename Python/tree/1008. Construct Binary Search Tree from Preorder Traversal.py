class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder):
        def helper(arr, min_val, max_val):
            if not arr or arr[0] < min_val or arr[0] > max_val:
                return None
            
            root_val = arr.pop(0)
            root = TreeNode(root_val)
            
            root.left = helper(arr, min_val, root_val)
            root.right = helper(arr, root_val, max_val)
            
            return root
        
        return helper(preorder, float('-inf'), float('inf'))
print(Solution().bstFromPreorder([8,5,1,7,10,12]))