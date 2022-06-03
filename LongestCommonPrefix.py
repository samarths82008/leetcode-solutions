class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        A = strs
        # default return value
        common = ""
        # check if input list is empty []
        if len(A) == 0:
            return common
        # if there is only one element [""], ["xyz"]
        if len(A) == 1:
            return A[0]
        # use the first string as a reference
        # check other strings, character by character
        for i, c in enumerate(A[0]):
            for s in A[1:]:
                # print(s, i)
                if len(s) < i+1 or s[i] != c:
                    return common

            common += c
                
        return common