'''给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        2. 动态规划
        3. 构造i，j 为index 长度的字符串 p[i][j] = True,最长的子串长度 j -i +1 
        4. p[i][i] = True, p[i][j] = True if j-i = 1 and s[i] == s[j]
        5. p[i][j] = p[i+1][j-1] and s[i] == s[j](字符串首尾相同)

        """
        n = len(s)
        dp = [[ False for _ in range(n)]for _ in range(n)]
        for ind in range(n):
            dp[ind][ind] = True # i==j 时 ，当个字符是回文

        ans = ""
        # 当前字符串的长度 length +1 
        for length in range(n):
            # 枚举子串的起始位置 ind_x ，这样可以通过 ind_y =ind_x +length 得到子串的结束位置
            for ind_x in range(n):
                ind_y  = ind_x  + length
                if ind_y >= len(s):
                    break
                if length == 0:
                    dp[ind_x][ind_y] = True
                elif length == 1:
                    dp[ind_x][ind_y] = (s[ind_x] == s[ind_y])
                else:
                    dp[ind_x][ind_y] = (dp[ind_x + 1][ind_y - 1] and s[ind_x] == s[ind_y])
                if dp[ind_x][ind_y] and length + 1 > len(ans):
                    ans = s[ind_x:ind_y+1]
        return ans



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        1. 暴力求解，遍历所有长度大于2的连续子串
        2. 如果没有的话，返回s[0]
        """
        if len(s) <2:
            return s
        def isvalid(tmp):
            start = 0
            end = len(tmp)-1
            while start < end:
                if tmp[start] != tmp[end]:
                    return False 
                start += 1
                end -= 1
            return True 

        res = s[0]
        max_ = 1
        # 比较所有字符串长度大于2的情况
        for ind_x in range(len(s)):
            for ind_y in range(ind_x+1,len(s)):
                if ind_y - ind_x +1 > max_ and isvalid(s[ind_x:ind_y+1]):
                    max_ = ind_y - ind_x + 1
                    res = s[ind_x:ind_y +1]
        
        return res 



