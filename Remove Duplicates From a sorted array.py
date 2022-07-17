class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        for w in range(1, len(nums)):
            if nums[w] != nums[w-1]:
                nums[i] = nums[w]
                i += 1
        return i
            