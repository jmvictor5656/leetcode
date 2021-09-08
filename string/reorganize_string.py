"""
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
from collections import Counter
from heapq import heappop, heappush

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = dict(Counter(s))
        maxHeap = []
        
        for char, freq in count.items():
            heappush(maxHeap, (-freq, char))
    
        prevChar, prevFreq = "", 0
        result = []
        
        # heappop current char so that it won't be used in next iter and again
        # add it to heap after process
        while maxHeap:
            freq, char = heappop(maxHeap)
            
            if prevChar and -prevFreq > 0:
                heappush(maxHeap, (prevFreq, prevChar))
            
            result.append(char)
            prevChar, prevFreq = char, freq + 1
            
        return "".join(result) if len(result) == len(s) else ""