'''
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。

 
示例 1：

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/russian-doll-envelopes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        最长子序列的升级版本，两维度的最长子序列

        """
        if not  envelopes:
            return 0 
        n = len(envelopes)
        # 按照宽度生序，按照长度 降序。同一个宽度最多只能选一个（严格大于）， 看长度的最长子序列了。
        envelopes = sorted(envelopes,key=lambda x:(x[0],-x[1])) # 
        f = [1]*n 
        for i in range(n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]: # 发现本身之前还有数字小于自己，可以套娃
                    f[i] = max(f[i],f[j]+1 ) # 动态规划 
        return max(f)
        



