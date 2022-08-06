class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0 
        while i >= 0:
            if i*i < x:
                i += 1
            elif i*i == x:
                return i
            else:
                return i-1
        