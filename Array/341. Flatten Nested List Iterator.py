"""
    Question:
        You are given a nested list of integers nestedList. 
        Each element is either an integer or a list whose elements may also be integers or other lists. 
        Implement an iterator to flatten it.
        Implement the NestedIterator class:
            NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
            int next() Returns the next integer in the nested list.
            boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
        Your code will be tested with the following pseudocode:
            initialize iterator with nestedList
            res = []
            while iterator.hasNext()
                append iterator.next() to the end of res
            return res
        If res matches the expected flattened list, then your code will be judged as correct.
"""

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
