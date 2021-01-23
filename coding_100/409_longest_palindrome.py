'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp_hash = {}
        for ind in s:
            if ind not in tmp_hash:
                tmp_hash[ind] = 1
            else:
                tmp_hash[ind]+= 1
        rst = 0 
        flag = True
        if len(tmp_hash) ==1:
            return len(s)
        for key,value in tmp_hash.items():
            
            
            rst += value // 2 *2 
            if rst %2 == 0 and value %2 == 1:  # 当前是偶数长度，才可以 +1 ，放在最中间形成回文。否则的话，就不能再增加一个
                rst += 1
        return rst  


                   
            
            
