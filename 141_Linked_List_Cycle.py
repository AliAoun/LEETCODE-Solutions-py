# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    

    # time complexity: O(n) where n is the number of nodes in the linked list. In the worst case, we may need to traverse the entire list.
    # space complexity: O(1) as we are using only a constant amount of extra space