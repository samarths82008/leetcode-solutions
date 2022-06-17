# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dictionary = { "}":"{",")":"(","]":"[" }
        oc = {"{" : 'o',"(" : 'o',"[" : 'o',")" : 'N',"]": 'c',"}" : 'c'}
        
        for i in s:
            if oc[i] == 'o':
                stack.append(i)
            else:
                try:
                    x = stack.pop()
                    if x == dictionary[i]:
                        continue
                    else:
                        return False
                # nothing in the stack - unmatched close
                except IndexError:
                    return False
        # string iterated, check if anything is unmatched
        if len(stack) == 0:
            return True
        else:
            return False
