class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left, right, max = 0, len(s) - 1, len(s)
        while left < right:
            while not s[left].isalnum():
                left += 1
                if left == max:
                    break
            while not s[right].isalnum():
                right -= 1
                if right < 0:
                    break
            if left == max and right < 0:
                return True
            elif left == max or right < 0:
                return False
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
                
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left, right, max = 0, len(s) - 1, len(s)
        while left < right:
            while left < max and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
            if left == max and right < 0:
                return True
            elif left == max or right < 0:
                return False
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
# inprovement on solution1. The logic of this algorithm is pretty simple. we only need to care about what causes False in this algorithm(alpha not equal). 
 class Solution(object):
 	def isPalindrome(self, s):
 		if not s:
 			return True
 		l, r = 0, len(s) - 1
 		while l < r:
 			while l < r and not s[l].isalnum():
 				l += 1
 			while l < r and not s[r].isalnum():
 				r -= 1
 			if s[l] != s[r]:
 				return False
 			else:
 				l += 1
 				r -= 1
 		return True

# solution two O(n) time and O(n) space
        if not s:
            return True
        washedS = []
        for item in s:
            if item.isalnum():
                washedS.append(item.lower())
        return washedS[::-1] == washedS