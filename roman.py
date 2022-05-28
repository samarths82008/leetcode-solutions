roman = {'I':1, 'V':5, 'X':10}
s = input("A roman numeral: ")
# string is an array or list
# you can interate and index into the string
if not isinstance(s, str):
    print("Input should be a string")
else:
    # initialize the number to output
    number = 0
    # reverse the input string
    s = s[::-1]
    # remember the last value
    last = None
    # go over the reversed string
    for i in range(len(s)):
        val = roman[s[i]]
        if last is None:
            number = val
            last = val
        elif last > val:
            number -= val
        else:
            number += val
            last = val
    print(number)
