class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if n % 3 != 0:
                res += 1
        return res
    
    # time complexity: O(n) as we are iterating through the list once
    # space complexity: O(1) as we are using only a constant amount of extra space