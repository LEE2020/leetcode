'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        牛顿法逼近 ， 二分查找法(根一定在0~x 之间的某个数，二分查找夹逼) ， 数学公式变换
        函数 f(x) = x^2 - c , 泰勒一阶展开 逼近 f(x) = f(x0) + (x-x0)f'(x0)
        令f(x) = 0 ,求c 就是根
        0 = f(x0) + (x-x0) * 2x0 
        x = 1/2(x0 + c/x0 )
        x 是 x0的逼近  
        """
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

"""
        left = 0
        right = x // 2 + 1
        ans = 0
        while left < right:
            
            mid = (left + right + 1)//2 
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
                ans = mid 
        # 因为一定存在，因此无需后处理
        return ans 
"""
"""
        if x == 0:
            return 0
        ans = int(math.exp(math.log(x)/2))
        return ans + 1 if (ans+1) ** 2 <= x else ans 
 """
