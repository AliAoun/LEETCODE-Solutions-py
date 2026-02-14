# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            x = math.gcd(current.val, current.next.val)

            new_node = ListNode(x)
            
            new_node.next = current.next
            current.next = new_node

            current = new_node.next

        return head
    
    # Time complexity: O(n log(max(a, b))) where n is the number of nodes in the linked list and a, b are the values of the nodes. The gcd function takes O(log(min(a, b))) time.
    # Space complexity: O(1) since we are modifying the linked list in place and not using any additional data structures that grow with the input size.