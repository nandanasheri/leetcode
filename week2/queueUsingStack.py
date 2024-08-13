class MyQueue(object):
    '''
    took me a while to figure out how to actually use a second container for my own benefit - everything is o(1) except for
    push - using the second container as a temporary storage as you reverse the order and add the new element to the very beginning
    so now the first element is on top of the list - first element on the stack to be popped and peeked at.
    '''

    def __init__(self):
        self.mainstack = []
        self.tempstack = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.tempstack = []
        for i in self.mainstack:
            self.tempstack.append(i)
        self.mainstack = []

        self.mainstack.append(x)

        for i in self.tempstack :
            self.mainstack.append(i)
        
        self.tempstack = []
        self.size += 1


    def pop(self):
        """
        :rtype: int
        """
        if self.size != 0:
            self.size -= 1
            return self.mainstack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.mainstack[self.size - 1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()