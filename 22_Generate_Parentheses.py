class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def btrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                btrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                btrack(openN, closeN + 1)
                stack.pop()

        btrack(0, 0)
        return res
