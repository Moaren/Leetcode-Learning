# Problem Descirption
- 94_Binary_Tree_Inorder_Traversal.md
- Given a binary tree, return the inorder traversal of its nodes' values.
**Example**:
```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
```

## Solution
### Takeawy:
1. How to solve tree problem using iteravtie method (stack/queue or DFS/BFS)
2. inorder/preorder/postorder 的前缀是针对root的先后顺序而言的，并且永远是先左后右，记得这个可以很快的回想起遍历顺序

### Recursive solution / original
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # boundary check
        if root == None: return []
        
        def travel(node):
            if node.left != None:
                travel(node.left)
            self.output.append(node.val)
            if node.right != None:
                travel(node.right)
        travel(root)
        return self.output
```

### *Iterative Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return []
        # boundary check
        # Reason why DFS require stack as the data structure
        
        stack = []
        curr = root
        output = []
        
        while stack != [] or curr != None:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        
        return output
```
