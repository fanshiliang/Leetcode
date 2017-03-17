class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        leftP = ["(","{","["]
        leftP = set(leftP)
        rightP = [")", "}", "]"]
        rightP = set(rightP)
        l, maxL, start = 0, 0, -1
        for index, item in enumerate(s):
            if item in leftP:
                stack.append(index)
            if item in rightP:
                if len(stack) > 0:
                    stack.pop()
                    if len(stack) > 0:
                        maxL = max(maxL, index - stack[-1])
                    if len(stack) == 0:
                        maxL = max(maxL, index - start)
                elif len(stack) == 0:
                    start = index
        return maxL
                          
                