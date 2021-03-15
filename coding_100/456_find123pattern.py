'''
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

注意：n 的值小于15000。

示例1:

输入: [1, 2, 3, 4]

输出: False

解释: 序列中不存在132模式的子序列。
示例 2:

输入: [3, 1, 4, 2]

输出: True

解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        如果当前元素比栈顶元素大，则将栈顶元素作为最小值记录。如果出现了比最小值的数，那就是出现了最小值，即 逆向是 2，3，1 ，正向就是1，3，2  了。 
        
        # 132 模式（数字之间可以间隔）
        stack = []
        MIN = float('-inf')
        for num in nums[::-1]:
            if num < MIN:
                return True 
            while stack and stack[-1] < num:
                MIN = stack.pop()
            stack.append(num)
        return False
        """ 

        # 满足结果的序列，数字之间可以断开
        length = len(nums)
        tmp = [nums[0]]
        for ind in range(length): # 以nums[ind]为轴心，寻找第一个更小的值
            tmp.append( min(nums[ind],tmp[-1]))
        stack = [] 
        for ind in range(length-1,-1,-1): #寻找第二小的值是否存在
            if nums[ind] > tmp[ind]:
                while stack and tmp[ind] >= stack[-1]:
                    stack.pop()
                #print(stack)
                if stack and nums[ind] > stack[-1]:
                    return True 
                stack.append(nums[ind]) # 新增的元素 永远在顶端，所以只需要比较stack[-1]
        return False
