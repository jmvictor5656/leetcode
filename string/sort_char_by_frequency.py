"""
451. Sort Characters By Frequency
Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of English letters and digits.
"""
from collections import Counter
from heapq import *

class Solution:
    def frequencySort(self, s: str) -> str:
        count = dict(Counter(s))
        minHeap = []
        
        for key, freq in count.items():
            heappush(minHeap, (freq, key))
        
        sorted_char = []
        
        while minHeap:
            char_count = heappop(minHeap)
            sorted_char.append(char_count[0]*char_count[1])
        
        return "".join(sorted_char[::-1])
