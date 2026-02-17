# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        ptr = head.next
        sum = 0
        while ptr.val != 0:
            sum += ptr.val
            ptr = ptr.next
        
        head.next.val = sum
        head.next.next = self.mergeNodes(ptr)
        
        return head.next
    
    # Time Complexity: O(n) where n is the number of nodes in the linked list.
    # Space Complexity: O(n) in the worst case due to recursive calls, where n is the number of nodes in the linked list. In the best case, it can be O(1) if there are no nodes between zeros.