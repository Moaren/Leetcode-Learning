# Problem Description
```
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
```

## TAKEAWAY
1. Consider the boundary conditions and put them at the front first
2. It is okay to use other data structure in such questions (hash table), as long as that structure is not too specific
3. The two-pointer method

## Hash Table Solution (mine)
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None: return False
        flag = False
        visited_hash = set()
        index = 0
        while not flag:
            if head == None:
                flag = False
                break
            if head not in visited_hash:
                visited_hash.add(head)
                index +=1 
            else:
                flag = True
                index +=1
            head = head.next
        return flag
```


## Two Pointer Solution
- Time complexity: O(n) Analysis:https://leetcode.com/problems/linked-list-cycle/solution/
- Space complexity: O(1)
- 性能更好
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None: return False
        slow = head
        fast = head.next
        
        while slow != fast:
            if (slow == None or fast == None) or fast.next == None:
            	# Note the boundary check here
            	# 官方都忘了！
                return False
            slow = slow.next
            fast = fast.next.next
        return True
```

