"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        left_side = []
        last = None

        # to get to the middle as 
        # well as reverse the linked
        # list of left side till middle
        while fast and fast.next:
            left_side.append(slow.val)
            current = slow
            slow = slow.next
            fast = fast.next.next
            current.next = last
            last = current
    
        left = last
        # odd case as for even it will
        # be none
        if fast:
            right = slow.next
        else:
            # even case
            right = slow
  
        status = True
        
        if not left or not right:
            return status

        # compare from left linked list to right list
        while left.val == right.val:
            left = left.next
            right = right.next
      
            if not left or not right:
                break
        else:
            status = False
        return status