# 516. Longest Palindromic Subsequence

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(dp)):
            dp[i][i] = 1
        
        for l in range(2, len(s)+1):
            for r in range(len(s) - l + 1):
                c = l + r - 1
                if l == 2 and s[r] == s[c]:
                    dp[r][c]=2
                elif s[r] == s[c]:
                    dp[r][c] = dp[r+1][c-1] + 2
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r+1][c])
        return dp[0][-1]