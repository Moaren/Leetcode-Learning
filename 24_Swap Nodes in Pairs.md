# Problem Description
- Given a linked list, swap every two adjacent nodes and return its head.

- You may not modify the values in the list's nodes, only nodes itself may be changed.

## Solution
### Takeaway
1. In linked list questions, the basic thing that can be modified is the single direction "next" pointer attached to each node. So all the problems can be transferred to how to express the spefic meaning by applying that modifcation properly.
2. The 'multiple assignment' feature in python can finish the pointer change in one time without confusing process.
3. One key to solve this problem is to clearly understand the pre->a->b->whatever reverse process. To understand this better, can refer to LeetCodeAnimation repo.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        backup = pre = ListNode()
        pre.next  = head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next,a.next,b.next =b, b.next,a
            pre = a
        return backup.next
```
