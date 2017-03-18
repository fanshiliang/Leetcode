class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ["(", "{", "["]
        right = [")", "}", "]"]
        stack = []
        for item in s:
            if item in left:
                stack.append(left.index(item))
            if item in right:
                if stack == [] or right.index(item) != stack.pop():
                    return False
        return stack == []