"""
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        string, pattern = s, p
        len_pattern, len_str =  len(pattern), len(string)
        if len_pattern > len_str:
            return []
  
        pattern_char_count = dict(Counter(pattern))

        window_char_counter = {}
        start = 0
        for end, char in enumerate(string):

            if char not in window_char_counter:
                window_char_counter[char] = 0
            window_char_counter[char] += 1

            if end - start + 1 > len_pattern:
                start_char = string[start]
                window_char_counter[start_char] -= 1

                if window_char_counter[start_char] == 0:
                    del window_char_counter[start_char]
                start += 1

            if window_char_counter == pattern_char_count:
                result.append(end - len_pattern + 1)
  
        return result
