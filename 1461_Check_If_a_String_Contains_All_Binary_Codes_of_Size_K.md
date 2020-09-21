# Problem Description
```
Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.
```
**Example 1:**
```
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
```

## Solution
### Takeaway:
1. 不要被惯性思维束缚，set等数据结构的引入会让解决bit maniputaion问题更加顺滑
2. 找unique value问题时刻记住应用set

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if s == "" and k == 0: return True
        
        s_len = len(s)
        s_int = int(s,2)
        
        start = 0
        substring_set = set()
        
        while start + k <= s_len:
            substring_set.add(int(s[start:start+k],2))
            start += 1
            if len(substring_set) >= 2**k: return True
        return False
```