'''
each elem NestedInteger - int/list
elem = 0
inner = 0
[[1,1],2,[1,1]]

      1
[1,[[[4]],[6, [3]]]]
           1

unpack_list (i, list):
    if i == len(list):
        return
    if [i] is an integer:
        return integer
    if [i] is a list:
        return unpack_list(i, list[0])

next ():
if [curr] isInteger:
    return that
    increment curr
else : (isList):
    list = getList() - must be recursive
    if inner < len(list):
        element = unpack_list(inner, list)
    if inner == len(list) - 1:
        # move to next element, reset inner index
        curr += 1
        inner = 0
    else:
        inner += 1

hasNext return curr < len(list)
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
        self.flatten = []
        self.currInd = 0
        for elem in nestedList:
            self._unpackList(elem)

        # print(self.flatten)

    def _unpackList (self, elem:[NestedInteger]):
        # base case
        if elem.isInteger():
            self.flatten.append(elem.getInteger())
            return
        # recursive case
        for i in range(len(elem.getList())):
            self._unpackList(elem.getList()[i])

    def next(self) -> int:
        val = self.flatten[self.currInd]
        self.currInd += 1
        return val
    
    def hasNext(self) -> bool:
        return self.currInd < len(self.flatten)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())