'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Example 4:
Input: s = "([])"
Output: true
Example 5:
Input: s = "([)]"
Output: false'''

from collections import deque 

class Solution(object):
    def isValid(self, s):
        stack = deque()
        pairs = {')':'(', ']': '[', '}':'{'}
        
        for p in s:
            if p in ('(', '[', '{'):
                stack.append(p)

            elif p in (')', ']', '}'):
                if not stack:
                    return False
                ultimo = stack.pop()
                if pairs[p] != ultimo:
                    return False

        return not stack
        

