'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

 

进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def 1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        利用unionfind 的思想将 i-1，i，i+1的序列找到 
        """
        longest = 0 
        hashset = set(nums)
        for num in hashset:
            if num -1 not in hashset:
                curr_num = num 
                curr_length = 1 
                while curr_num + 1 in hashset:
                    curr_num  += 1
                    curr_length += 1
                longest = max(longest,curr_length)
        return longest

