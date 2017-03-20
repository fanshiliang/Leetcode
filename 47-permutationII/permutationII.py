class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    #Solution one use visited list. Time complexity O(n^n)
        nums.sort()
        self.result = []
        visited = [0 for n in range(len(nums))]
        self._perm(nums, [], visited)
        return self.result
    #Solution two use swap, Time complexity O(n!)

    def _perm(self, nums, res, visited):
        if len(res) == len(nums):
            self.result.append(res)
            return
        for index in range(len(nums)):
            if visited[index]:
                continue
            if index > 0 and nums[index] == nums[index - 1] and not visited[index - 1]:
                continue
            visited[index] = 1
            self._perm(nums, res + [nums[index]], visited)
            visited[index] = 0
    
    def _perm2(self, nums, i):
        if i == len(nums) - 1:
            self.result.append(nums[::])
            return
        for k in range(i, len(nums)):
            if k != i and nums[i] == nums[k]:
                continue
            nums[i], nums[k] = nums[k], nums[i]
            self._perm(nums[::], i + 1)

