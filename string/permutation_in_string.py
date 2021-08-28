"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
Accepted
209.7K
Submissions
469.1K
Seen this question in a real interview before?
"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2) -> bool:
        string = s2
        pattern = s1
        len_pattern, len_str =  len(pattern), len(string)
        if len_pattern > len_str:
            return False

        pattern_char_count = dict(Counter(pattern))

        window_char_counter = {}
        start = 0
        for end, char in enumerate(string):

            if char not in window_char_counter:
                window_char_counter[char] = 0
            # add char in front of window
            window_char_counter[char] += 1

            # remove char from end of window 
            if end - start + 1 > len_pattern:
                start_char = string[start]
                window_char_counter[start_char] -= 1

                if window_char_counter[start_char] == 0:
                    del window_char_counter[start_char]
                start += 1

            if window_char_counter == pattern_char_count:
                return True

        return False

