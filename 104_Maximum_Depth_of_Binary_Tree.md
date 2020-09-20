# Problem Description
- 104_Maximum_Depth_of_Binary_Tree.md
- Given a binary tree, find its maximum depth.
- The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
- Note: A leaf is a node with no children.
- Example:
- Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
```

## Solution
### Takeaway
- How to write a public varaible (class parametr)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_val = 0
        
    def maxDepth(self, root: TreeNode) -> int:
        
        def dig(node,n):
            if node != None:
                n += 1
                if n > self.max_val: self.max_val = n
                dig(node.left,n)
                dig(node.right,n)
            else:
                return None
        dig(root,0)
        return self.max_val
```