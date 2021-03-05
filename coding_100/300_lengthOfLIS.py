'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # dp[i][j] 的值代表 nums的起始位置，和终止位置 
        动态规划
        """
        if len(nums) < 2:
            return len(nums)
        dp = [1] * len(nums)

        for ind in range(len(nums)):
            for  ind2 in range(ind):
                if nums[ind2] < nums[ind]:
                    dp[ind] = max(dp[ind],dp[ind2]+1)
        return max(dp )

"""
        if len(nums) < 2:
            return len(nums)
        dp = [[ [] for _ in range(len(nums))   ] for _ in range(len(nums))]
        # 初始化 dp
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    
                    dp[i][j].append(nums[i])
        ## 只有下一个值超过了 dp中的值最后一个时，才添加到dp中
        for ind in range(len(nums)):
            for ind2 in range(ind+1,len(nums)):
                if nums[ind2] > dp[ind][ind2-1]:
                    dp[ind][ind2] = dp[ind][ind2].append(nums[ind2])
                else:
                    dp[ind][ind2] = dp[ind][ind2-1]
        return dp

"""
