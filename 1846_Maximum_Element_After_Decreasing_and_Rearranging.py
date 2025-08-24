class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0

        for n in arr:
            prev = min(prev + 1, n)
        return prev
    
    # time complexity = O(n log n), due to sorting and binary search 
    # space complexity = O(1) due to constant space usage