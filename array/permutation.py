"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append([])
        
        for num in nums:
            for _ in range(len(queue)):
                old_permutation = queue.popleft()
                
                for i in range(len(old_permutation)+1):
                    new_permutation = list(old_permutation)
                    new_permutation.insert(i, num)
                    
                    if len(new_permutation) == len(nums):
                        result.append(new_permutation)
                    else:
                        queue.append(new_permutation)
        return result
