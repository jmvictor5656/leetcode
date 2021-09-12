"""
143. Reorder List

ou are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        last = None

        while fast and fast.next:
            # current = fast
            last = slow
            fast = fast.next.next
            slow = slow.next
    # current.next = last
    # last = current
        if not head.next:
            return head
        last.next = None
        last = None
        middle = slow

        # divide linked list in two parts
        # and inverse the right side
        while middle:
            current = middle
            middle = middle.next
            current.next = last
            last = current
    
        return_head = head
        while last and head:
            current_last_next = last.next
            current_head_next = head.next
            head.next = last
            last.next = current_head_next
            # for odd case right left side will be even
            # but right one hase extra node(odd) due to
            # slow and fast pointer approach
            if not current_head_next:
                last.next = current_last_next
            head = current_head_next
            last = current_last_next
 
        return return_head
