"""
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        pattern_count = dict(Counter(t))

        win_counter = {}
        win_status = {}
        start, end = 0, 0
        result = ""
        min_length = float('inf')
        
        while end < len(s):
            end_char = s[end]

            if end_char in pattern_count:
                if end_char not in win_counter:
                    win_counter[end_char] = 0
                win_counter[end_char] += 1

                if win_counter[end_char] >= pattern_count[end_char]:
                    win_status[end_char] = True
      
            # iterativing status updater using win_status using len  of win_status
            # reset win_status once one len is calculated
            if len(win_status) == len(pattern_count):

                # shrink window till result is valid
                while start < end:
                    start_char = s[start]
                    if start_char in pattern_count and win_counter[start_char]-1 >= pattern_count[start_char]:
                        win_counter[start_char]-=1
                        start += 1
                    elif start_char not in pattern_count:
                        start += 1
                    else:
                        break
                if min_length > end - start + 1:
                    result = s[start:end+1]
                    min_length = end - start + 1
            end += 1
        return result
