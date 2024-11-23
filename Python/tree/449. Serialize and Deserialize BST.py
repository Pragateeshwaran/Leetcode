class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
# ------------------------------ DFS ------------------------------------------------------
class Codec:
    def serialize(self, root) -> str:
        if not root: return "#"
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    def deserialize(self, data: str):
        def helper(queue):
            val = queue.pop(0)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = helper(queue)
            node.right = helper(queue)
            return node
        queue = data.split(',')
        return helper(queue)
    
# ------------------------------ BFS ------------------------------------------------------

class Codec:
    def serialize(self, root):
        if not root:
            return ""
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")
        return ",".join(result)

    def deserialize(self, data: str):
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if values[i] != "#":
                left = TreeNode(int(values[i]))
                node.left = left
                queue.append(left)
            i += 1
            if values[i] != "#":
                right = TreeNode(int(values[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# print(ans)