# Problem Description
```
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
```

## Solution
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def get_size(head):
            i = 1
            while head.next != None:
                i += 1
                head = head.next
            return i
        if head == None:return None
        length = get_size(head)
        mid = length//2
        i = 0
        while(i < mid):
            head = head.next
            i += 1
        return head
```

## Answer**
- TAKEAWAY: 
	- a = b = c in Python means a = c; b = c
	- Faster than mine.(1.5n vs 0.5n) The thinking is interesting also.
```Python
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```