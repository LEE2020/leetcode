'''
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 1:
            return [s]
        rst = []

        for ind,tmp in enumerate(s):
            res_s = s[:ind]+s[ind+1:]
            for ind2 in self.permutation(res_s): # self.permutation(res_s) 返回了 bc,cb ,当tmp = a 
                if str(tmp)+str(ind2) not in rst:
                    rst.append(str(tmp)+str(ind2))

        return rst 


''' 
利用递归的思想，将整体排序划分为更小的序列排序
当长度为1时，返回本身。
其他情况，利用遍历本身 + 剩余的序列 （剩余的序列又可以本身 + 剩余的序列）
完成递归'''

