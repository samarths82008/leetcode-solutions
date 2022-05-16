class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hash table to map values to indices
        Dictionary = {}
        # go over all the entries in the list
        for index, value in enumerate(nums):
            # if 2nd pair (target - value) is in dictionary
            # then return current index & 2nd pair index
            if target - value in Dictionary:
                return Dictionary[target - value], index
            else:
                # update the dictionary with the current value/index pair
                Dictionary[value] = index