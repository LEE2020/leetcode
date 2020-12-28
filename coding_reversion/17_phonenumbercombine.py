'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        key = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        if digits == '':
            return []
        ans=['']
        for num in digits:
            ans = [pre + suf for pre in ans for suf in key[num]]
        return ans 




        '''
        if len(digits)==0:
            return None
        elif len(digits)==1:
            if digits=='1':
                return None
            elif digits=='2':
                return 'abc'
            elif digits=='3':
                return 'def'
            elif digits=='4':
                return 'ghi'
            elif digits=='5':
                return 'jkl'
            elif digits=='6':
                return 'mno'
            elif digits=='7':
                return 'pqrs'
            elif digits =='8':
                return 'tuv'
            elif digits=='9':
                return 'wxyz'
        else:
            #ind = len(digits)
            tmp = digits.pop()
            return self.letterCombinations(digits)+[x for x in tmp] '''
