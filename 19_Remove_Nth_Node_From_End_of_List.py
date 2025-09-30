# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        l = dummyNode
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return dummyNode.next
    
    # Time Complexity: O(n) where n is the number of nodes in the linked list and we traverse the list once.
    # Space Complexity: O(1) due to the use of constant space.