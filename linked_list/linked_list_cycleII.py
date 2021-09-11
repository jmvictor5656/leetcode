"""
142. Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # using rabit, tortoise approach
        slow, fast = head, head
        length_of_cycle = 0
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # cycle found so get circumference of linked list
                length_of_cycle = self.get_cycle_length(slow)
                break
        else:
            # if no cycle return
            return
        
        node1, node2 = head, head
        
        # move node 2 equal to cicumference of linked list
        # as it started from head so now it is same distance
        # apart from entry point of linked list as from head
        while length_of_cycle:
            node2 = node2.next
            length_of_cycle -= 1
        
        # as node2 is same distance apart to reach entry point of
        # linked list as from head, so there entry point will be
        # the entry point of linked list
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
        
        return node1
    
    def get_cycle_length(self, node):
        current = node
        length = 0
        
        while True:
            current = current.next
            length += 1
            
            if current == node:
                break
        return length
