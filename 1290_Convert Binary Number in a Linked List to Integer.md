# Problem Description
```
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
```

## Solution
### Takeaway
- 涉及链表其实不多，更多的是基本的位运算思想，学习这种表达形式
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans << 1 | head.val
            head = head.next
        return ans
```
