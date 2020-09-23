# Problem Description
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

```
Example
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

## Solution
1. 这道题的思路事实上非常直观，即优先找出各个深度下最靠右的val依次填入output当中。基于这个基本思路有三个space和time complexity都差不多的方法，即递归、stack,queue
2. 递归：最先想出来的写法，比较直观。主要构建难点在于想清楚每一步的步骤和顺序，以及想明白迭代过程中要比较的depth以什么样的形式进行传递
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_layer = 0

    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:return []

        output = []

        def travel(node,layer):
            if node == None: return None
            else:
                layer += 1
                if layer > self.max_layer:
                    self.max_layer += 1
                    output.append(node.val)
                travel(node.right,layer)
                travel(node.left,layer)
        travel(root,0)
        return output
```
3. stack: 本质等价于DFS,在tree问题中一般遍历顺序是先左后右，因此使用DFS求解时只需保证记录每一个点对应的depth。同一层depth下最先被处理的必定就是我们要的解(即“后入先出”的右端)。
	a. dict.setdefult(key,val) 与直接赋值的区别在于如果原dict存在对应的key-value对 只会返回旧value而不会更新dict（很关键的一个function）
	b. 每一层遍历下对right后进行操作，pop时自动就能保证永远先右后左
	c. 学习这种同时记录val和depth的思路
```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:return []

        rightmost_value_at_depth = dict()
        max_depth = -1

        stack = [(root,0)]

        while stack:
            node,depth = stack.pop()
            
            if node is not None:
                max_depth = max(max_depth,depth)

                rightmost_value_at_depth.setdefault(depth,node.val)

                stack.append((node.left,depth+1))
                stack.append((node.right,depth+1))
        
        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]
```
4. queue:first in first out, 本质等价于BFS，在tree问题中BFS会优先访问并处理左侧，因此只要不停刷新max_val对应的每一层depth的取值，最后遍历完的结果就是想要的。
	a. from collections import deque
	b. queue.popleft()
	c. 处理顺序在这个问题里和stack是一致的，与tree要求的访问顺序相同，核心区别在于rightmost_value_at_depth是一锤定音还是持续进行更新
```python
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict()
        max_depth = -1

        queue = deque([(root,0)])

        while queue:
            node,depth = queue.popleft()
            
            if node is not None:
                max_depth = max(max_depth,depth)
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
    

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]
```
5. 和这个题相似的是94 Binary Tree Inorder Traversal  