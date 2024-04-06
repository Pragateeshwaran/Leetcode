class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dictionary = {}
        
        def dfs(node):
            if node in dictionary:
                return dictionary[node]
            
            value = Node(node.val)
            dictionary[node] = value
            for i in node.neighbors:
                value.neighbors.append(dfs(i))
                
            return value
        
        if node:
            return dfs(node)
        return None
# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Define node relationships
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Create the solution object
solution = Solution()

# Clone the graph starting from node1
cloned_node = solution.cloneGraph(node1)

# Print the original and cloned graph values
def print_graph(node):
    visited = set()
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(f"Node {current.val} neighbors: {[neighbor.val for neighbor in current.neighbors]}")
            visited.add(current)
            queue.extend(current.neighbors)

print("Original graph:")
print_graph(node1)

print("Cloned graph:")
print_graph(cloned_node)

