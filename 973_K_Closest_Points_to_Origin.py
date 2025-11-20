class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res
    
    # Time Complexity: O(n + k log n) , explaination is that we are pushing all n points into the heap which takes O(n) time
    # and then we are popping k points from the heap which takes O(k log n)
    # Space Complexity: O(n) for the heap