#  Search a 2D Matrix

#  Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix[0]:
            return False
        
        for array in matrix:
            if(array[0] <= target <= array[-1]):
                return self.binary_search(array, target, 0, len(array))
        return False        
    
    def binary_search(self, array, target, start, end):
        if start > end:
            return False
        mid = (start + end)//2
        
        if array[mid]==target:
            return True
        elif array[mid]<target:
            return self.binary_search(array, target, mid+1, end)
        elif array[mid]>target:
            return self.binary_search(array, target, start, mid -1)