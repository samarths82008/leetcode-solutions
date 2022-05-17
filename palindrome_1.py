class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x2 = x[::-1]
        if x == x2:
            return True
        else:
            return False