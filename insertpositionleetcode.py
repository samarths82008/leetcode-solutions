class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            else:
                i += 1
        if nums[i-1] < target:
            return i