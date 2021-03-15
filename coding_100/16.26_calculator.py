'''
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/calculator-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
********************************************************************
解决 1-1 +1 case 中的负号问题。
将负号转成 +-4的形式 
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        # 后缀表达式（中缀转后缀，逆波兰表达式）
        """
        return self.cal(s)

    def  cal(self,s):
        ''' 根据后缀表达式 计算结果 例如 3,2,2,*,+ '''
        tmp = self.postfix_s(s)
        stack = [] 
        for ind in range(len(tmp)):
            
            #print(str(tmp[ind]).isdigit())
            #num.lstrip('-').isdigit()
            if str(tmp[ind]).lstrip('-').isdigit() :
            #if str(tmp[ind]) not in ['+','-','*','/']:
                stack.append(tmp[ind])
            else:
                #print(stack)
                val2 = stack.pop()
                val1 = stack.pop()
                if tmp[ind]   == '*':stack.append(val1 * val2 )
                elif tmp[ind] == '/':
                    t = abs(val1)/abs(val2)
                    if val1*val2 <0: t = -t 
                    stack.append(t)
                elif tmp[ind] == '+':stack.append(val1 + val2)
                elif tmp[ind] == '-':stack.append(val1 - val2 ) 
               
        return stack[0] 

            

        
    def getPriority(self,tmp):
        if str(tmp) in[ '*', '/']:
            return 2 
        elif str(tmp) in[ '+','-']:
            return 1 
        else:
            return 0 

    def postfix_s(self,s):
        ''' 中缀转后缀'''
        ans = []
        ops = []
        flag_neg = 1 
        flag_continue_numeric = 0 
        for ind in range(len(s)):
            if s[ind] ==' ':continue  
            elif s[ind] >='0' and s[ind]<='9' and flag_continue_numeric ==0  :
                ans.append(int(s[ind])*flag_neg)
                flag_continue_numeric = 1 
                
            elif s[ind] >='0' and s[ind]<='9' and flag_continue_numeric ==1: 
                #tmp1 = ans.pop()
                tmp = 10*int(ans.pop()) + int(s[ind])*flag_neg 
                ans.append(tmp)
                
        
            elif(s[ind] == '+' or s[ind] == '-' or s[ind] == '*' or s[ind] == '/'):
                flag_continue_numeric = 0 
                    
                if not ops:
                    if s[ind] =='-':
                        ops.append('+')
                        flag_neg = -1 
                    else:
                        ops.append(str(s[ind]))
                        flag_neg = 1 
                else:
                    flag_neg = 1 
                    if s[ind] =='-' :
                        flag_neg = -1 
                    if self.getPriority(str(s[ind])) > self.getPriority(ops[-1]):
                        ops.append(str(s[ind]))
                    else:
                        #print(ops,str(s[ind]),self.getPriority(str(s[ind]))<=self.getPriority(ops[-1]))
                        while  ops and self.getPriority(str(s[ind])) <= self.getPriority(ops[-1]):                       
                            ans.append(ops.pop()) 
                        if s[ind] == '-': 
                            ops.append('+')
                        else:
                            ops.append(str(s[ind]))
        #print(ans,ops)
        while  ops:
            ans.append(ops.pop())          
        return  ans
