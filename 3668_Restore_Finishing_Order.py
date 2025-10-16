class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        lst = []
        for i in order:
            if i in friends:
                lst.append(i)
        return lst
    
    # Time Complexity: O(n * m) where n is the length of 'order' and m is the length of 'friends'.
    # Space Complexity: O(n) for storing the result in 'lst'.