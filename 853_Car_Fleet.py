class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, spped)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if stack >= 2 and stack[-1] <= stack[-2]:
                stack.pop
        return len(stack)
    
    # time complexity: O(n log n) due to sorting and iterating through the list
    # space complexity: O(n) due to the stack used to store the time taken for each car to reach the target