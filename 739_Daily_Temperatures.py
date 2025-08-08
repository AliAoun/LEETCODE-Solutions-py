class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0] * len(temperatures)
        # stack = []

        # for i, t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackT, stackInd = stack.pop()
        #         res[stackInd] = (i - stackInd)
        #     stack.append([t, i])
        # return res 
        res = [0] * len(temperatures)
        stack = []
        stack.append(0)

        for i in range(1,len(temperatures)):
            while stack and temperatures [i]> temperatures[stack[-1]]:
                prev=stack.pop()
                res[prev]=i-prev
            stack.append(i)

        return res
    
    # time complexity: O(n) where n is the length of temperatures
    # space complexity: O(n) for the stack and result list