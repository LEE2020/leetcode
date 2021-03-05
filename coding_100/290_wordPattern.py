'''
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        相互映射
        """
        p2s = {}
        s2p = {} 
        s = s.split(' ')
        if len(pattern) != len(s):
            return False 
        
        for p_tmp ,s_tmp in zip(pattern,s):
            if p_tmp in p2s and p2s[p_tmp] != s_tmp or s_tmp in s2p and s2p[s_tmp] != p_tmp:
                return False 
            p2s[p_tmp] = s_tmp 
            s2p[s_tmp] = p_tmp 
        return True 


