"""
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""

# using linked list based slow and fast pointer approach
class Solution:
    def isHappy(self, num: int) -> bool:
        dp = {}
        slow = num
        fast = num
        result = True

        while True:
            fast =  self.get_multiple(fast, 2, dp)
            if fast == 1:
                break

            slow = self.get_multiple(slow, 1, dp)
            if fast == slow:
                result = False
                break

        return result

    def get_multiple(self, num, hop, dp):
        """
        hop -> n_times u want to repeat
        """
        while hop:
            digit_list = list(map(int, list(str(num))))
            if num not in dp:
                dp[num] = sum([n**2 for n in digit_list])
            num = dp[num]
            hop -=1
        return num

