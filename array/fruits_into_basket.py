"""
Problem Statement#
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

def fruits_into_baskets(fruits):
  start = 0
  counter = {}
  max_len = 0

  for i, end in enumerate(fruits):
    max_len = max(max_len, i - start +1)
    if end not in counter:
      counter[end] = 1
    else:
      counter[end] += 1
    
    if len(counter) > 2:
      # while len(counter) > 2:
      #   if counter[fruits[start]] > 0:
      #     counter[fruits[start]] -= 1
      #   elif counter[fruits[start]] == 0:
      del counter[fruits[start]]
      
      while fruits[start] not in counter:
        start += 1
  return max_len
