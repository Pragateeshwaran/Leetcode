class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        """
        Splits the linked list into k parts as evenly as possible.

        :param head: ListNode - The head of the linked list.
        :param k: int - The number of parts to split the list into.
        :return: List[ListNode] - A list containing the heads of the split parts.
        """
        ans = []
        temp = head
        count = 0
        
        # Count the number of nodes in the list
        while temp:
            count += 1
            temp = temp.next
        
        equal = count // k  # Minimum number of nodes per part
        extra = count % k   # Extra nodes to distribute among the first 'extra' parts
        
        prevHead = head
        
        for _ in range(k):
            t = equal
            if extra > 0:
                t += 1
                extra -= 1
            
            newHead = prevHead
            for _ in range(t - 1):  # Traverse the current part
                if newHead:
                    newHead = newHead.next
            
            if newHead:
                nextHead = newHead.next
                newHead.next = None  # Cut the current part from the rest
                ans.append(prevHead)
                prevHead = nextHead
            else:
                ans.append(None)  # If no more nodes, append None
        
        return ans
# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
parts = solution.splitListToParts(node1, 3)
 
# Print each part of the split list
for i, part in enumerate(parts):
    print(f"Part {i+1}:")
    print_linked_list(part)
