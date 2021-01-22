'''
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
示例 1:

输入: "()"
输出: True
示例 2:

输入: "(*)"
输出: True
示例 3:

输入: "(*))"
输出: True

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parenthesis-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        star = []
        for ind in range(len(s)):
            if s[ind] =='(':
                left.append(ind)
            elif s[ind] =='*':
                star.append(ind)
            else:
                if len(left)!=0:
                    left.pop()
                elif len(star) != 0:
                    star.pop()
                else:
                    return False 
        if len(left) ==0 :
            return True
        elif len(left) > len(star):
            return False 
        else:
            while left:
                tmp1 = left.pop()
                tmp2 = star.pop()
                if tmp1 > tmp2:
                    return False
        return True  if len(left) == 0 else False 

        

