# Problem Description
 Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1. The root is the maximum number in the array.
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree. 

Example:
```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```

## Solution
### Takeaway
1. How to write recursion for tree problem
2. Take not of the index change when the processing list has changed
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []: return None
        def construct(nums,l,r):
            if l == r: return None
            sub_nums = nums[l:r]
            max_val = max(sub_nums)
            index = nums.index(max_val)
            root = TreeNode(max_val)
            root.left = construct(nums,l,index)
            root.right = construct(nums,index+1,r)
            return root
        return construct(nums,0,len(nums))
```