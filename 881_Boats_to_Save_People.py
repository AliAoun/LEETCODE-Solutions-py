class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats, l, r = 0, 0, len(people) - 1
        
        while r >= l:
            if (people[r] + people[l]) > limit:
                boats += 1
                r -= 1
                
            else:
                boats += 1
                l += 1
                r -= 1

        return boats
    
    # time complexity: O(n log n) due to sorting
    # space complexity: O(1) since we are using constant space for pointers and counters