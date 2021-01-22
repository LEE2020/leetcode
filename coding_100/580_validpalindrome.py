'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
通过次数60,667提交次数152,145

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

验证的时候，用双指针的方法，从start,end逼近。 若两边相同，start +1 ,end-1. 否则看子问题 s[start+1,end] 或者s[start,end-1]
看这两个的情况
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(s,start,end):
            i = start 
            j = end
            while i<j:
                if s[i] != s[j]:
                    return False 
                i += 1
                j -= 1
            return True
        start = 0 
        end = len(s)-1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return check(s,start+1,end ) or check(s,start,end-1)


        return True

