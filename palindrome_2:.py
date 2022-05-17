class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        end = len(x) - 1
        begin = 0
        while end > begin:
            if x[begin] != x[end]:
                return False
            begin += 1
            end -= 1
        return True
