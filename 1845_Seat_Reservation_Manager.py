class SeatManager:

    def __init__(self, n: int):
        self.unres = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.unres)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unres, seatNumber)

    # time complexity: O(log n) for both reserve and unreserve
    # space complexity: O(n) for storing unreserved seats in a heap

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)