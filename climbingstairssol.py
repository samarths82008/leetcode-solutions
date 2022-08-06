class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        prevPrev = 1
        prev = 2
        current = 0
        for step in range(3, n+1):
            current = prevPrev + prev
            prevPrev = prev
            prev = current
        return current