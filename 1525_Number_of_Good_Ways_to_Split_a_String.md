# Problem Descrition
```
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.
```

**Example 1:**
```
Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
```

## Solution:
### Takeaway:
1. 掌握 ord(string) - 97 将字母转化为编码的技巧
2. 记住这种构建letter table的思路，可以将space complexity从O(N)转化为O(1)
3. 如果一个正序的table解决不了问题，尝试加入另一个反序的可能会有奇效
4. 通过letter table对比是否相同，方法是count(1)
5. a = b = []的多重赋值是地址传递，因此如果是想构造两个独立的list不能这么用，必须分开创立

```python
class Solution:
    def numSplits(self, s: str) -> int:
        # boundary condition
        if s == None:return 0
        if len(s) <=1 :return 0
        
        arr_l = [0 for _ in range(26)]
        arr_r = [0 for _ in range(26)]
        
        for i in s:
            arr_l[ord(i) - 97] += 1
        
        result = 0
        for idx in range(len(s)-1,-1,-1):
            arr_r[ord(s[idx]) - 97] += 1
            arr_l[ord(s[idx]) - 97] -= 1
            if arr_r.count(0) == arr_l.count(0):
                result += 1
        return result
```
