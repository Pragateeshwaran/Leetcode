# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def swapPairs(self, head):
#         dummy = ListNode(0)
#         dummy.next = head
#         curr = dummy
#         while curr.next and curr.next.next:
#             temp1 = curr.next
#             temp2 = temp1.next
#             curr.next, temp1.next, temp2.next = temp2, temp2.next, temp1
#             curr = temp1
#         return dummy.next
class Solution:
    def swapPairs(self, head):
       
        curr_slow = head
        if curr_slow:
            curr_fast = curr_slow.next
            while curr_fast:
                if curr_fast.next:                
                    temp1 = curr_fast.next
                    temp2 = temp1.next
                else:
                    temp1 = None
                    temp2 = None
                curr_slow.val, curr_fast.val = curr_fast.val, curr_slow.val
                curr_slow, curr_fast = temp1, temp2
        return head
# 1 2 3 4 
# 2 1 4 3 
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
a = Solution().swapPairs(head)
while a:
    print(a.val)
    a = a.next
