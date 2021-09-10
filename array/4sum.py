"""
18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        result = []
        
        for i1 in range(len(nums)-3):
            if i1 > 0 and nums[i1-1] == nums[i1]:
                continue
            for i2 in range(i1+1, len(nums)-2):
                if i2 > i1+ 1 and nums[i2-1] == nums[i2]:
                    continue
                num1, num2 = nums[i1], nums[i2]
                
                i3, i4 = i2+1, len(nums)-1
                
                while i3<i4 and i4 < len(nums):
                    num3, num4 = nums[i3], nums[i4]
                    
                    
                    
                    total = num1 + num2 + num3 + num4
                    
                    if total == target:
                        
                        result.append([num1, num2, num3, num4])
                        i3 += 1
                        while i3 < i4 and nums[i3-1] == nums[i3]:
                            i3 += 1
                        while i3 < i4 and i4+1 < len(nums) and nums[i4+1] == nums[i4]:
                            i4 -= 1
                    elif total < target:
                        i3 += 1
                    elif total > target:
                        i4 -= 1
        return result
