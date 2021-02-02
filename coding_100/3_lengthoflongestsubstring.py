'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        利用滑动窗口，记录最长不包含重复的字符串长度
        一旦相等，则将相等的字符及之前的字符全部划出窗口，当前字符串长度减少
        再新增后续字符，同时记录长度 
        
        """
        tmp_set = set()
        max_len = 0 
        tmp_len = 0 
        left = 0 
        for ind in range(len(s)):
            tmp_len += 1 
            while s[ind] in tmp_set:
                tmp_set.remove(s[left]) # 删除出现重复的字符，及它之前的字符
                left += 1 
                tmp_len -=  1 # 划出窗口的字符，长度需要减1 

            if tmp_len > max_len:
                max_len = tmp_len  # 保留历史最长的字符串长度 
            tmp_set.add(s[ind])

        return max_len 

