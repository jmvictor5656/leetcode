# 494. Target Sum
# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def top(nums, target, i, cur_sum):
            if (i, cur_sum) in dp:
                return dp[(i,cur_sum)]
            if target == cur_sum and i == len(nums):
                return 1
            if i >= len(nums):
                return 0


            sum1 = top(nums, target, i+1, cur_sum-nums[i])
            sum2 = top(nums, target, i+1, cur_sum+nums[i])
            dp[(i,cur_sum)] = sum1+sum2
            return dp[(i,cur_sum)]
        
        return top(nums, target, 0, 0)
        