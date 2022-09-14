# create a bst as well as print left and right side of tree
array = [8, 3, 10, 1, 6, 7, 4, 14, 13, 11, 15]
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
    
    def insert_node(self, val, parent=None):
        if not self.root:
            self.root = Node(val)
        else:
            if parent.val < val:
                if parent.right:
                    self.insert_node(val, parent.right)
                else:
                    parent.right = Node(val)
            elif parent.val > val:
                if parent.left:
                    self.insert_node(val, parent.left)
                else:
                    parent.left = Node(val)
    
    def create_bst(self, array):
        for num in array:
            self.insert_node(num, self.root)
            
    
    def view(self):
        queue = deque()
        queue.append(self.root)
        
        right = []
        left = []
        
        while queue:
            n = len(queue)
            
            curr_level = []
            
            for _ in range(n):
                node = queue.popleft()
                
                curr_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if curr_level:
                right.append(curr_level[-1])
                left.append(curr_level[0])
        return left,right

bst = BST()
bst.create_bst(array)
print(bst.view())
