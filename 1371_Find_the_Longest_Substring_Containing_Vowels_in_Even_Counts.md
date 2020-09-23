# Problem Description
```
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
```

## Solution
1. 实际上得到这个解法有一段思考迭代过程，大致概括一下就是：前缀和差值法（统计前i个当中各个元音出现的次数，取i-j的差值即为s[i:j]的情况）+ 奇偶数出现次数差值的规律(偶数-偶数=偶数，奇数-奇数=偶数) = 用bitmap表示前i个数字的奇偶状态。只要特定的奇偶状态出现过一次，直接取序数差值即可
2. 注意这种规定dp table和采用位移法模拟bitmap的方法
3. 初始值的设立非常重要，本身只有一个字母的情况也应该考虑，因此lis[0] = 0，lis[1] = 1
```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        if s == "" or s == None: return 0
        
        lis = [-1 for i in range(2**5)]
        
        status = 0
        ans = 0

        lis[0] = 0
        for i in range(len(s)):
            if s[i] == "a":status ^= 1<<0
            elif s[i] == "e": status ^= 1<<1
            elif s[i] == "i": status ^= 1<<2
            elif s[i] == "o": status ^= 1<<3
            elif s[i] == "u": status ^= 1<<4

            if lis[status] >= 0: 
                ans = max(ans,i + 1  - lis[status])
            else:
                lis[status] = i + 1

        return ans
```