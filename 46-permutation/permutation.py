class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self._perm(nums, [])
        return self.result
        
    def _perm(self, nums, res):
        if not nums:
            self.result.append(res)
        else:
            for index in range(len(nums)):
                self._perm(nums[:index] + nums[index + 1:], res + [nums[index]])
        