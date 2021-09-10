"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        
        for i1 in range(len(nums)-2):
            i2, i3 = i1+1, len(nums) - 1
            
            while i2 < i3:
                num1, num2, num3 = nums[i1], nums[i2], nums[i3]
                
                diff = target - sum([num1, num2, num3])
                
                if diff == 0:
                    return target
                
                if abs(diff) < abs(min_diff):
                    min_diff = diff
                
                if diff > 0:
                    i2 += 1
                if diff < 0:
                    i3 -= 1
        return target - min_diff
