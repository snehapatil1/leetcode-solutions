"""
    Data Structures: Array
    Time Complexity: O(n)
    Space Complexity: O(n2)
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat:
            return mat
        
        if (len(mat) * len(mat[0])) != r * c:
            return mat
        
        new_matrix = []
        temp = []

        for x in mat:
            for y in x:
                temp.append(y)

        current_index = 0
        for row in range(r):
            new_matrix.append(temp[current_index:current_index+c])
            current_index = current_index+c

        return new_matrix
