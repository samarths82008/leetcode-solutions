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