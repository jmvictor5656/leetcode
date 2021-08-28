"""
Problem Statement#
Given a string, find the length of the longest substring, which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""

def non_repeat_substring(str):
  if len(str) < 1: return 0

  start = 0
  seen = {}
  max_len = 0

  for end, char in enumerate(str):
    if char not in seen:
      seen[char] = True
      max_len = max(max_len, end - start + 1)
    else:
      start = end

  return max_len
