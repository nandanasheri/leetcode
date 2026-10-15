'''
Stack Based Solution
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in range ((len(nestedList)-1),-1,-1):
            # append to stack in reverse because LIFO
            self.stack.append(nestedList[i])

    def next(self) -> int:
        # guaranteed to be an Integer because hasNext is called before next()
        val = self.stack.pop().getInteger()
        return val
    
    def hasNext(self) -> bool:
        while self.stack and (not self.stack[-1].isInteger()):
            l = self.stack.pop().getList()
            for i in range(len(l)-1,-1,-1):
                self.stack.append(l[i])
        if self.stack:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())