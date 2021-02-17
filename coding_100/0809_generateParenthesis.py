'''括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bracket-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        生成合法的括号，只要（ 有，就需要填写（， 一旦右边的数量比左边的多，需要填写 ）
        递归
        """
        rst = []
        nleft = nright = n 
        def dfs(nleft,nright,tmp_str):
            if (len(tmp_str) == 2* n):
                rst.append(tmp_str)
                return rst 
            if (nleft > 0):
                dfs(nleft-1,nright,tmp_str + '(')
            if (nleft < nright):
                dfs(nleft,nright-1,tmp_str+')')
        dfs(n,n,'')
        return rst 




