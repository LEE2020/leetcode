'''
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # 三位数组 来表示交易过程中的状态 
        # dp[i][j][k]  第i天，第j次交易， k=【买入/卖出】状态 0 表示买入，1表示卖出 
        # dp[i][j][0] 在第i天，交易了j次，此时是买入状态 
        # dp[i][j][1] 在第i天，交易了j次，此时是卖出状态
        # 且在卖出时，增加1次交易次数 
        if not prices or not k:
            return 0 
        n = len(prices)
        dp = [[[0 for ind in range(2)] for _ in range(k+1)] for _ in range(len(prices))]
        res = [] 
        # 当k . n//2 时 可认为是不限次数的交易
        if k > n//2:
            return self.greedy(prices)

        for ind in range(k+1):
            dp[0][ind][0] = -prices[0] # 买入
            dp[0][ind][1] = 0   # 卖出（没有资产，卖出没有利润）
        for i in range(1,n):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i-1][j][0] , dp[i-1][j][1] - prices[i])

                if j==0: # 不产生卖出，不交易次数
                    dp[i][j][1] = dp[i-1][j][1]
                else:
                    dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0] + prices[i])
                
        for ind in range(k+1):
            res.append(dp[n-1][ind][1])
        return max(res)
    def  greedy(self,prices):
        res = 0 
        for ind in range(1,len(prices)):
            if prices[ind] - prices[ind-1] >0:
                res += prices[ind]-prices[ind-1]
        return res 
