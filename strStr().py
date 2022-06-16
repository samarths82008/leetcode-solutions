class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        #first loop that checks if i is smaller then the length of haystack
        while i < len(haystack):
            k = 0
        # second loop does the same but for k
            while k < len(needle):
                if i+k >= len(haystack) or needle[k] != haystack[i+k]:
                    break
                k += 1
        # checks if k has reached the final length   
            if k == len(needle):
                return i
            i += 1
        
        return -1