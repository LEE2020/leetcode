'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_t = {} 
        for ind,num  in enumerate(nums):
            res = target - num 
            if res in hash_t:
                return [hash_t[res],ind]
            else:
                hash_t[num] = ind 



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rst = []
        for ind1 in range(len(nums)):
            for ind2 in range(ind1,len(nums)):
                if ind1 == ind2: continue
                if nums[ind1] + nums[ind2] == target:
                    rst.append(ind1)
                    rst.append(ind2)
                    break

        return rst



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_t = {} 
        for ind in range(len(nums)):
            hash_t[nums[ind]] = ind  # 序列中元素要不相同
        rst = []
        start = 0 
        end = len(nums) -1 
        nums = sorted(nums)
        while start < end:
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                rst.append(hash_t[nums[start]])
                rst.append(hash_t[nums[end]])
                break

        return rst 



        

        

