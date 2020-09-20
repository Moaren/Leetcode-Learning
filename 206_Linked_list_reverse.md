# Problem Description
Reverse a singly linked list.

## Takeaway
When deal with linked list, be careful about the relation change (attach/disattach) among nodes.

## Iterative Solution
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while(cur != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
```

### Attempt 2
- 基本思路是一样的，只不过这种是以after为中心
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:return head        
        cur = head
        after = head.next
        while after.next != None:
            temp = after.next
            after.next = cur
            cur = after
            after = temp
        after.next = cur
        head.next = None
        return after
```



## Recursive Solution
### Recursion 1:
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        return self.reverse(cur,prev)
    
    def reverse(self,cur,prev):
        if cur == None:
            return prev
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        return self.reverse(cur,prev)
```

### Recursion 2:
- Because **head.next = None** happens before the **after.next = head** and this method iterate one by one. So it doesn't matter here for each step.
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # first for boundary check; second for end condition
        if head == None or head.next == None:return head
        recursive_node = self.reverseList(head.next)
        after = head.next
        after.next = head
        head.next = None
        return recursive_node
```

