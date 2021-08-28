"""
Longest Substring with maximum K Distinct Characters
Problem Statement#
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
Example 4:

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
"""


def longest_substring_with_k_distinct(str1, k):
  # TODO: Write your code here
  counter = {}
  start, max_len = 0, 0

  for end, char in enumerate(str1):
    if char not in counter:
      counter[char] = 0
    counter[char] += 1

    if len(counter) > k:
      while len(counter) > k:
        start_char = str1[start]
        counter[start_char] -= 1
        start += 1

        if counter[start_char] == 0:
          del counter[start_char]
    max_len = max(max_len, end - start +1)

  return max_len
