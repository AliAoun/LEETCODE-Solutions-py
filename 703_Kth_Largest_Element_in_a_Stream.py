class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K-Largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq,heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
    # Time Complexity: O(log K) for add(). Bcz it pushes/pops from a heap of size k, O(N log K) for __init__()
    # Space Complexity: O(K), the heap never grows beyond k elements, so it uses O(k) space

###############################################################

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


