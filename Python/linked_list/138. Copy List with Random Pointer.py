# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Create a dictionary to map original nodes to their copies
        node_map = {}
        
        # First pass: Create a copy of each node and store it in the dictionary
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass: Update the next and random pointers of the copy nodes
        curr = head
        while curr:
            copy_node = node_map[curr]
            if curr.next:
                copy_node.next = node_map[curr.next]
            if curr.random:
                copy_node.random = node_map[curr.random]
            curr = curr.next
        
        # Return the head of the copied linked list
        return node_map[head]

# Create nodes
nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]

# Set next pointers
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

# Set random pointers based on the indices provided in the input
random_indices = [None, 0, 4, 2, 0]

for i in range(len(nodes)):
    if random_indices[i] is not None:
        nodes[i].random = nodes[random_indices[i]]

# Create a Solution instance and call the copyRandomList method
solution = Solution()
copied_head = solution.copyRandomList(nodes[0])

# Print the values of the copied linked list
while copied_head:
    print(copied_head.val)
    copied_head = copied_head.next
    
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]