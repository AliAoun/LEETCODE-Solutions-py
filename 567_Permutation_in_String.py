from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for i in range(len(s2) - len(s1) + 1):
            c_s = s2[i:i+len(s1)]
            if Counter(c_s) == Counter(s1) :
                return True
        return False 
    
    # time complexity: O(n * m) where n is the length of s2 and m is the length of s1
    # space complexity: O(m) for the Counter objects
    # a slow solution but I'll try to optimize it later

    


    # Optimized sliding window approach with O(n) time complexity
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            end_char = s2[i]
            window_count[end_char] += 1
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                del window_count[start_char]
            if window_count == s1_count:
                return True
        
        return False
   







    