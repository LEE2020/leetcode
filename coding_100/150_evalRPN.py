'''
150. 逆波兰表达式求
根据 逆波兰表示法，求表达式的值。

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

 

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
 

示例 1：

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = [] 
       
        operations = ['*','+','-','/']
        for ind in range(len(tokens)):
            if  tokens[ind] not in operations:
                stack.append(int(tokens[ind]))
            else:
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                if tokens[ind] =='+': 
                    stack.append(tmp2 + tmp1)
                elif tokens[ind]=='-':
                    stack.append(tmp2 - tmp1)
                elif tokens[ind] =='*':
                    stack.append(tmp2 * tmp1)
                elif tokens[ind] =='/':
                    stack.append(int(tmp2/float(tmp1))) # python 向下取整
                    
                    
                

        return stack[-1]


            
