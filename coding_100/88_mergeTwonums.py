'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # O(M+N), O(1)
        p = m-1 
        q = n-1 
        r = m+n -1

        #nums1 += n*[0]
        while p >=0 and q>=0:
            if  nums1[p] < nums2[q]:
                nums1[r] = nums2[q]
                q-= 1 
            else:
                nums1[r] = nums1[p]
                p -= 1 
            r -= 1 
        nums1[:q+1] = nums2[:q+1] # 从0 到q+1的位置上的数据，如果nums2没有遍历的话，说明都比nums1小
        return nums1








