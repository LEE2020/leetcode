'''
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-i-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution(object):
    
    def permutation(self, S): 
        """
        :type S: str
        :rtype: List[str]
        ### 组合的方法 超时 ！！
        """
        rst = []
        if len(S) == 1:
            return S 
        for ind in range(len(S)):
            curr = S[ind]
            others = S[:ind] + S[ind+1:]
            for ind2 in self.permutation(others):  # 在剩余的字符串中递归，返回长度为1的时候的字符串，和当前的字符串组合
                if curr + ind2 not in rst:
                    rst.append(curr+ind2)
        return rst 
        
    def permutation(self,S):
        if S == '' : return []
        res = [] 
        path = '' 
        def helper(S,path,res):
            if S == '' : 
                res.append(path)
                return 
            for ind in range(len(S)):
                cur = S[ind]
                helper(S[:ind] + S[ind+1:],cur + path , res )  # 递归的思路，路径
        helper(S,path,res )
                
        return res

