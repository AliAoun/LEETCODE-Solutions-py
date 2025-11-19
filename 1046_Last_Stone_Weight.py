class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, (first - second))
        
        return abs(stones[0]) if stones else 0
    
    # Time Complexity: O(n log n) where n is the number of stones
    # Space Complexity: O(n) for the heap storage