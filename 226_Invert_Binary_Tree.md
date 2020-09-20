# Problem Description
226_Invert_Binary_Tree.md
- Invert a binary tree
- This problem was inspired by this original tweet by Max Howell:
> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

## Solution
经典
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # boundary condition
        
        def invert(node):
            if node == None:return None
            temp = node.left
            node.left = node.right
            node.right = temp
            invert(node.left)
            invert(node.right)
        invert(root)
        return root
```