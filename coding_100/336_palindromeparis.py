'''
给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

 

示例 1：

输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]] 
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2：

输入：["bat","tab","cat"]
输出：[[0,1],[1,0]] 
解释：可拼接成的回文串为 ["battab","tabbat"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        overtime!!!
        """
        def valid(x_str,y_str):
            tmp = x_str + y_str 
            return tmp == tmp[::-1]
        rst = [] 
        for ind in range(len(words)):
            for ind_2 in range(len(words)):
                if ind == ind_2:
                    continue
                if valid(words[ind],words[ind_2]):
                    rst.append([ind,ind_2])
        return rst 




