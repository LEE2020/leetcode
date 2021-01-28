'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
 
最小的数，最小的应当排在前面，对于字符串来说 ‘30’<'5' 

依据字符串的大小比较： x + y < y + x = > x < y 

利用快排对字符串进行从小到大排序，然后直接拼接起来，就可以了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        #将nums 转换成str, 对str排序
        # 字符串 x + y < y + x 则 x < y 
        arr = [str(tmp) for tmp in nums ]
        def quick_sort(arr):
            if len(arr)<=1:
                return arr
            else:
                pivot = arr[0]
                length = len(arr)
                swap_pos = 0+1 
                for ind in range(1,length):
                    if arr[ind] + pivot < pivot  + arr[ind]: # ==》 arr[ind] < pivot 的字符串 
                        arr[ind],arr[swap_pos] = arr[swap_pos],arr[ind]
                        swap_pos += 1
                arr[0],arr[swap_pos-1] = arr[swap_pos-1],arr[0]
                left_ = quick_sort(arr[:swap_pos-1])
                right_=quick_sort(arr[swap_pos:])
                left_.append(arr[swap_pos-1])
                return left_ + right_ 
        return ''.join( [ (itemp) for itemp in quick_sort(arr)])
