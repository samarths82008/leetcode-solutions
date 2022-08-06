class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = s.split()
        if len(p) == 0:
            return None
        else:
            return len(p[-1])