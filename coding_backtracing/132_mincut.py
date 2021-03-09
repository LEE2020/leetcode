'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。

 

示例 1：

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
示例 2：

输入：s = "a"
输出：0
示例 3：

输入：s = "ab"
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        dp 节省时间开销
        """


        size = len(s)
        if size < 2:
            return 0

        dp = [i for i in range(size)]
        check_palindrome = [[False for _ in range(size)] for _ in range(size)]

        for right in range(size):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left + 1][right - 1]):
                    check_palindrome[left][right] = True

        for i in range(1, size):
            if check_palindrome[0][i]:
                dp[i] = 0
                continue
            # 枚举分割点
            dp[i] = min([dp[j] + 1 for j in range(i) if check_palindrome[j + 1][i]])

        return dp[size - 1]





    """   
       # 超时 
        res = []
        self.backtrack(s, res, [])
        return min(res)

    def backtrack(self, s, res, path):
        if not s:
            res.append(len(path)-1)
            return
        for i in range(1, len(s) + 1): #注意起始和结束位置
            #if self.isPalindrome(s[:i]):
            if s[:i] == s[:i][::-1]:
                self.backtrack(s[i:], res, path + [s[:i]]) # path = [[s[:i]],[]]
    """
