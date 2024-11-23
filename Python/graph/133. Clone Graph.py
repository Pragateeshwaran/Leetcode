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



from typing import Optional, Dict
from collections import deque

class Node:
    """Graph node with value and list of neighbors."""
    def __init__(self, val: int = 0, neighbors: list = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Clone a graph using BFS approach.
        Time complexity: O(V + E) where V is number of vertices and E is number of edges
        Space complexity: O(V) for the hash map and queue
        """
        if not node:
            return None

        # Dictionary to store the mapping of original nodes to their clones
        clones: Dict[Node, Node] = {}
        
        def bfs_clone(start: Node) -> Node:
            queue = deque([start])
            clones[start] = Node(start.val)
            
            while queue:
                curr = queue.popleft()
                
                for neighbor in curr.neighbors:
                    # Create clone for new nodes
                    if neighbor not in clones:
                        clones[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    
                    # Connect cloned nodes
                    clones[curr].neighbors.append(clones[neighbor])
            
            return clones[start]
        
        def dfs_clone(node: Node) -> Node:
            """Alternative DFS approach to clone the graph."""
            if node in clones:
                return clones[node]
                
            clone = Node(node.val)
            clones[node] = clone
            
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs_clone(neighbor))
                
            return clone
        
        # Use BFS by default as it's generally more space-efficient for wide graphs
        return bfs_clone(node)
    
    def verify_clone(self, original: Optional[Node], clone: Optional[Node]) -> bool:
        """
        Verify if the cloned graph is identical to the original.
        Returns True if the clone is correct, False otherwise.
        """
        if not original and not clone:
            return True
        if not original or not clone:
            return False
            
        visited_orig = set()
        visited_clone = set()
        queue = deque([(original, clone)])
        
        while queue:
            orig, cln = queue.popleft()
            
            if orig.val != cln.val:
                return False
                
            if len(orig.neighbors) != len(cln.neighbors):
                return False
                
            visited_orig.add(orig)
            visited_clone.add(cln)
            
            # Create sets of neighbor values for O(1) lookup
            orig_neighbor_vals = {n.val for n in orig.neighbors}
            clone_neighbor_vals = {n.val for n in cln.neighbors}
            
            if orig_neighbor_vals != clone_neighbor_vals:
                return False
                
            # Check unvisited neighbors
            for o_neighbor, c_neighbor in zip(orig.neighbors, cln.neighbors):
                if o_neighbor not in visited_orig:
                    queue.append((o_neighbor, c_neighbor))
        
        return True

    @staticmethod
    def create_test_graph() -> Node:
        """Create a sample graph for testing."""
        nodes = [Node(i) for i in range(4)]
        
        # Create connections: 0-1-2-3-0 (circular)
        nodes[0].neighbors = [nodes[1], nodes[3]]
        nodes[1].neighbors = [nodes[0], nodes[2]]
        nodes[2].neighbors = [nodes[1], nodes[3]]
        nodes[3].neighbors = [nodes[2], nodes[0]]
        
        return nodes[0]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Create test graph
    test_graph = solution.create_test_graph()
    
    # Clone graph
    cloned = solution.cloneGraph(test_graph)
    
    # Verify clone
    is_correct = solution.verify_clone(test_graph, cloned)
    print(f"Clone verification: {'Passed' if is_correct else 'Failed'}")