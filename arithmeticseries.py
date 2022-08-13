class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        k = 0
        a = len(nums)-1
        total = 0
        while k < a:
            if nums[k] + diff in d and nums[k] + 2*diff in d:
                total += 1    
            k += 1
