# 32 longest valid parentheses

题目链接：https://leetcode.com/problems/longest-valid-parentheses/#/description

想到了两种解决方法：

## 方法一：使用stack，算法时间复杂度O(n), 空间复杂度O(n).

​	思路如下：从头到尾遍历字符串，遇到左括号就将左括号的index压入栈中。遇到右括号，考虑如下情况：

1.   如果当前栈中有左括号，则将栈顶左括号弹出。此时，有两种情况需要考虑：

     - [x] 左括号出栈之后，此时栈中还有左括号，则此时更新maxL

           ```python
           maxL = max(maxL, index - stack[-1])
           ```

     - [x] 左括号出栈之后，当前栈中没有数据，则说明所有左括号与右括号匹配。为了计算length，引入变量start，start初始默认为-1. 当右括号多的时候，更新start为右括号的index，后面讨论。此时，更新maxL为

           ```python
           maxL = max(maxL, index - start)
           ```

     ​

	2. 如果当前栈中没有左括号，此时说明string中，右括号多与左括号，当前计算的最长子序列应该截止于此。但是我们没法判断之后还有没有子序列，我们可以认为直到出现左括号之前，不会有子序列的产生。所以我们更新start为右括号的index。

    ```python
    start = index
    ```

以上就是这个方法的整体思路。整体算法如下：

```python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #solution one O(n) time and O(n) space
         stack = []
         leftP = ["(","{","["]
         leftP = set(leftP)
         rightP = [")", "}", "]"]
         rightP = set(rightP)
         l, maxL, start = 0, 0, -1
         for index, item in enumerate(s):
             if item in leftP:
                 stack.append(index)
             if item in rightP:
                 if len(stack) > 0:
                     stack.pop()
                     if len(stack) > 0:
                         maxL = max(maxL, index - stack[-1])
                     if len(stack) == 0:
                         maxL = max(maxL, index - start)
                 elif len(stack) == 0:
                     start = index
         return maxL
```

## 方法二：从左到右各遍历一次，算法时间复杂度O(n), 空间复杂度O(1)

算法思路：先从左往右遍历字符串，遇到左括号left += 1， 遇到右括号 right +=1. 如果right > left参数，则将left 和 right参数重置为0. 也就是右括号先于左括号出现，不可能出现子序列，所以重置。如果left == right时，更新maxL。因此从左往右遍历，可以检查出所有 右括号比左括号多的情况下的最长子序列。但是没有考录左括号比右括号多的情况。所以，我们还需要从右往左遍历一次。具体代码如下所示：

```python
#solution two O(n) time and O(1) space
        left, right, maxL = 0, 0, 0
        for item in s:
            if item == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxL = max(maxL, 2 * right)
            if right > left:
                left = right = 0
        left = right = 0
        for item in s[::-1]:
            if item == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxL = max(maxL, 2 * left)
            if left > right:
                left = right = 0
        return maxL
```

