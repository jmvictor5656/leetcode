"""
257. Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
Accepted
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.rec(root, result, [])
        return result
    def rec(self, root, result, path):
        if not root:return ''
        
        path.append(str(root.val))
        if not root.right and not root.left:
            result.append("->".join(path))
    
        if root.right:
            self.rec(root.right, result, path)
        
        if root.left:
            self.rec(root.left, result, path)
        
        del path[-1]
