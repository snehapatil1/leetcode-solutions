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
        def flattenList(nested_List):
            for ele in nested_List:
                if ele.isInteger():
                    self._integers.append(ele.getInteger())
                else:
                    flattenList(ele.getList())
        
        self._integers = []
        self._position = -1
        flattenList(nestedList)
    
    def next(self) -> int:
        self._position += 1
        return self._integers[self._position]
    
    def hasNext(self) -> bool:
         return self._position + 1 < len(self._integers)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
