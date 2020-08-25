# Problem Description
```
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
```

## Initial Solution (not recommanded)
This solution is not recommanded since it atucally makes use of Python list's indexing feature. That means to solve a linked list problem, a more complex structure is introduced. That is not very proper and kind of loses meaning of such problem alr.
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Boundary check
# Read key question conditions carefully
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:return None
        if head.next == None:return head
        prev_list = []
        after_list = []
        while head != None:
            if head.val >=x:
                after_list.append(head)
            else:
                prev_list.append(head)
            head = head.next
        prev_list.extend(after_list)
        i = 0
        length = len(prev_list)
        while i < length-1:
            prev_list[i].next = prev_list[i+1]
            i += 1
        prev_list[-1].next = None
        return prev_list[0]
```

## Solution
- TAKEAWAY:
	- For multiple assignment (a=b=c=someClass())), the result passed here is actually address, which means a,b,c will be the same class instead of three classes with the same attributes
	- Consider both conditions ending with before or after. If the last element is in before list, after.next = None will be necessary.
	- Remeber how to create a new empty ListNode - new_node = ListNode(0)
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head != None:
            if head.val >= x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next
            head = head.next
            
        after.next = None
        before.next = after_head.next
        return before_head.next
```