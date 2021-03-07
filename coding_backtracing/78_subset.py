'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        顺序组合种类
        if len(nums) == 1:
            return [nums]
        res = [] 
        for  ind in range(len(nums)):
            others = nums[:ind] + nums[ind+1:]
            curr = nums[ind]
            for ind2 in self.subsets(others):
                res.append([curr] + ind2 )
        return res 
        """
        
        res = []
        n = len(nums)
          
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res 

        """
        rst = [[]]
        tmp = []
        for ind in nums:
            tmp = [ind2 + [ind] for ind2 in rst] 
            for ind2 in tmp:
                if ind2 not in rst:
        
                    rst += tmp 
        return rst
        """
