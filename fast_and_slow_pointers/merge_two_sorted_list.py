# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

# Example 1:


# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: l1 = [], l2 = []
# Output: []
# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        merges two sorted linked list
        """
        result = []
        next_l1 = l1
        next_l2 = l2

        while not next_l1==None or not next_l2==None:
            if not next_l1 == None and not next_l2 == None:
                minimum = min(next_l1.val, next_l2.val)
            elif not next_l1 == None:
                minimum = next_l1.val
            else:
                minimum = next_l2.val
            
            minimum_node = None
            if not next_l1 == None and minimum == next_l1.val:
                minimum_node = next_l1
                next_l1 = next_l1.next
            else:
                minimum_node = next_l2
                next_l2 = next_l2.next
            result.append(minimum_node)
        return self.create_list_node(result)
    
    def create_list_node(self, array):
        """
        creates a linked list
        """
        if not array:
            return
        for i in range(len(array)-2, -1, -1):
            array[i].next = array[i+1]
        return array[0]
    
    