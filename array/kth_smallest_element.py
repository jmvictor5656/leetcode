"""
378. Kth Smallest Element in a Sorted Matrix
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
"""
from heapq import heappop, heappush

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count, number = 0, -1
        minHeap = []
        
        for list in matrix:
            heappush(minHeap, [list[0], 0, list])
            
        
        while minHeap:
            number, index, list = heappop(minHeap)
            count += 1
            
            if count == k:
                break
            
            if index + 1 < len(list):
                heappush(minHeap, [list[index+1], index+1, list])
        return number
