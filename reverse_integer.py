"""
Source : https://leetcode.com/problems/reverse-integer/description/
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if int is negative, make it positive. I'll make it negative later
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        
	# converting to string
	# I know I could've used % to get the last digit of the string, but this was just easier
        convString = str(x)
        digit = ""
        while len(convString) > 0:
            digit += convString[-1]
            convString = convString[:-1]
            
        
        convInt = int(digit)
	# make negative is it was originally negative
        if negative:
            convInt = convInt * -1
	# if int overflowed, return 0
	# I coouldve check if the variable is still int ( python automatically converts to long when overflowing) 
        if convInt > 2147483647 or convInt < -2147483647:
            return 0
        
        return convInt
