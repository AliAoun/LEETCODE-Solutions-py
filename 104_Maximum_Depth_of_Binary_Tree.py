# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #### DFS Recursive Approach: ###
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Time Complexity: O(N) where N is the number of nodes in the binary tree. Due to the fact that we visit each node exactly once.
    # Space Complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (a completely unbalanced tree), the height of the tree could be N, leading to O(N) space complexity. In the best case (a balanced tree), the height would be log(N), leading to O(log N) space complexity.






        #### DFS Iterative Approach: ###
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
        return res
    
    # Time Complexity: O(N) where N is the number of nodes in the binary tree. Due to the fact that we visit each node exactly once.
    # Space Complexity: O(H) where H is the height of the binary tree. This space is used by the stack. In the worst case (a completely unbalanced tree), the height of the tree could be N, leading to O(N) space complexity. In the best case (a balanced tree), the height would be log(N), leading to O(log N) space complexity.