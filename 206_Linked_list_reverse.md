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

## Recursive Solution
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