# 96. Unique Binary Search Trees

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

# Example 1:


# Input: n = 3
# Output: 5
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 19
# Accepted
# 387.6K
# Submissions
# 696.2K
# Seen this question in a real interview before?

class Solution:
    def __init__(self):
        self.mem = {0:1, 1:1, 2:2}
        
    def numTrees(self, n: int) -> int:
        if n<0:
            return 0
                    
        if n in self.mem:
            return self.mem[n]
        
        total = 0
        
        for i in range(1, n+1):
            root = i
            left_n_tree = i - 1
            right_n_tree = n - i
            
            total += self.mem[left_n_tree]*self.numTrees(right_n_tree)
            
        self.mem[n] = total
        return self.mem[n]