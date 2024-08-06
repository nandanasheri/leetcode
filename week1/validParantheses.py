class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Basic Stack solution - few edge cases to account for here what i learnt is list.append() and list.pop() 
        are both o(1) so this is o(n) complexity. use a deque for o(1) add and remove from both ends.
        '''
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' or i == ']' or i == '}':
                if (len(stack) == 0):
                    return False
                topofstack = stack[-1]
                if i == ')' and topofstack != '(':
                    return False
                elif i == '}' and topofstack != '{':
                    return False
                elif i == ']' and topofstack != '[':
                    return False
                stack.pop()
        
        if len(stack) == 0:
            return True
        return False