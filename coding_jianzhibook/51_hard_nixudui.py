'''在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5

需要排序的次数，采用merge sort 来解决 
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        def  mergesort(nums):
            if len(nums)==1:
                return nums,0 
            middle = len(nums)//2
            left,count1 = mergesort(nums[:middle])
            right,count2 = mergesort(nums[middle:])
            all_nums,count3 = merge(left ,right)

            return all_nums,(count1+count2+count3) 
        def merge(left,right):
            rst = []
            cnt = 0
            while len(left) >0 and len(right)>0:
                if left[0] <= right[0]:
                    rst.append(left[0])
                    left.remove(left[0])

                elif left[0] > right[0]:
                    rst.append(right[0])
                    right.remove(right[0])
                    cnt = cnt + len(left)
                
            if len(left) ==0:
                rst += right 
            else:
                rst += left 
            return rst,cnt 
        _,cnt = mergesort(nums)
        return cnt
