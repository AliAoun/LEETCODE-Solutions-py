class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (sum(nums) % k)
    
    # Time Complexity: O(n) where n is the length of the input array nums.
    # Space Complexity: O(1) since we are using only a constant amount of extra space to store the sum and the result.