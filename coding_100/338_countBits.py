'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        奇数 就是
        举例：
          2 = 10       4 = 100       8 = 1000
          3 = 11       6 = 110       12 = 1100
        举例： 
         0 = 0       1 = 1
         2 = 10      3 = 11
        奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。
        偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。
    链接：https://leetcode-cn.com/problems/counting-bits/solution/          hen-qing-xi-de-si-lu-by-duadua/
        动态规划
        """

        dp=[0]*(num+1)
        for i in range(num+1):
            if(i%2==1):
                dp[i]=dp[i-1]+1
            else:
                dp[i]=dp[i//2]
        return dp

