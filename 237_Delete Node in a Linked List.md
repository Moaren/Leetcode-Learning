# Problem Description
需要结合给的例子：https://leetcode.com/problems/delete-node-in-a-linked-list/

## Solution
- 被人吐槽是个烂题，某种意义上也确实是...思路还是挺有意思的
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while 1:
            temp = node.next
            node.val = temp.val
            if temp.next == None:
                node.next = None
                break
            node = temp
```