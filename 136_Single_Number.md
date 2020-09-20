# Problem Description
- Given a **non-empty** array of integers, every element appears twice except for one. Find that single one.
- **Note**: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

```
Input: [2,2,1]
Output: 1
```

## Solution
### Original / Hash table
- 没啥可说的 O(n) O(n)
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums == []: return None
        dic = {}
        for i in nums:
            if i in dic: dic[i] += 1
            else: dic[i] = 1
        for key in dic:
            if dic[key] == 1: return key
```

### *Bit Manipulation*
- 也没啥可说的 能用想到xor的这个性质很牛逼就完了 O(n) O（1）
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums == []: return None
        result = 0
        for num in nums:result ^= num
        return result
```