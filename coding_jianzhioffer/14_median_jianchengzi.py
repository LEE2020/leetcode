'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

第n次剪的绳子，在n-1次的基础上，选择max的情况，可以使用动态规划来实现 
每次剪到位置越靠近中间，相乘越大
max(maxvalue, t*(l-t),t*dp(l-t)) 



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==2:
            return 1
        if n==3:
            return 2
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        for ind_x in range(4,n+1):
            maxValue = 0
            for ind_y in range(1,ind_x//2+1):
                maxValue = max(maxValue,(ind_y)*(ind_x-ind_y) , (ind_y)*dp[ind_x - ind_y ])
            dp[ind_x] = maxValue
            
        return dp[n] 
