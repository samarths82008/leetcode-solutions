class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        x = len(s)
        num = roman_map[s[x - 1]]
        for i in range(x - 2, -1, -1): 
            if roman_map[s[i]] >= roman_map[s[i + 1]]:
                num += roman_map[s[i]]
            else:
                num -= roman_map[s[i]]
        return num