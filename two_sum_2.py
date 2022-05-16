class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        end = len(nums)
        for f in range(len(nums)-1):
            for s in range(f+1, end):
                if nums[f] + nums[s] == target:
                    return f, s