'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000

使用快排，来确定中位数的pos

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None 
        # 改变nums的排列，使得middle对应着nums的中位数
        def partition(nums,length,start,end):
            ''' based  on quick sort , return pos of array[pivot]'''
            pivot = nums[start]
            swap_pos = start+1
            for ind in range(start+1,end):
                if nums[ind]<pivot:
                    nums[ind],nums[swap_pos] = nums[swap_pos],nums[ind]
                    swap_pos += 1 
            nums[swap_pos-1],nums[start] = nums[start],nums[swap_pos-1]
            return swap_pos-1 

        length = len(nums)
        middle = length>>1 
       
        start = 0 
        end = length 
        index = partition(nums,length,start,end)
       
        while index != middle:
            if index > middle:
                end = index -1 
                index = partition(nums,length,start,end)
               
            else:
                start = index + 1
                index = partition(nums,length,start,end)
               
       
        result = nums[middle]
         
        return result


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for tmp in nums:
            if tmp not in dic:
                dic[tmp] = 1
            else:
                dic[tmp] += 1
        rst = [key for key,value in dic.items() if value > len(nums)/2]
        return rst[0] 





