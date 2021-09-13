"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.

class Solution:
    def reverseKGroup(self, head, k: int):
        if k == 1:
            return head

        last_list_end, current_list_start, current_list_end, next_list_start = None, head, None, None
        
        counter = 1
        current = head 
        
        while current:
            if counter % k == 0:
                next_list_start = current.next
                # disconnecting the list for flowless iteration
                current.next = None
                rev_start, rev_end = self.reverse(current_list_start)

                if last_list_end:
                    # connecting with end of previous linked list
                    # to reversed start node
                    last_list_end.next = rev_start
                else:
                    # for beginning of list
                    head = rev_start
                
                # connecting end of reversed list to remaining list that 
                # need to be processed
                rev_end.next = next_list_start
                current_list_start = next_list_start
                last_list_end = rev_end
                # as list has reversed so current also point to last value
                current = rev_end
            
            current = current.next
            counter += 1
        return head
    def reverse(self, head) -> [ListNode, ListNode]:
        end = head
        
        last, current, next = None, head, None
        
        while current:
            next = current.next
            current.next = last
            last = current
            current = next
        
        newStart = last
        return newStart, end

# array = [1,2,3,4,5]
# # start = None, la
# nodes = [ListNode(val=i) for i in array]
# for i in range(len(array)-1):
#     nodes[i].next = nodes[i+1]

# s = Solution()
# print(s.reverseKGroup(nodes[0], 2))