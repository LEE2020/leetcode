'''
这里有 n 个航班，它们分别从 1 到 n 进行编号。

我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [j, k, l] 意味着我们在从 j 到 k 的每个航班上预订了 l 个座位。

请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。

 

示例：

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/corporate-flight-bookings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        cur time 的当前的流量
        cur[i] += cur[i-1] 截止到i时刻，的流量

        """
        """
        length = len(bookings)
        cur_seats = [0]*n
        for ind in range(length):
            start,end,num = bookings[ind]
            for ind2 in range(start,end+1):
                cur_seats[ind2-1] += num 

        return cur_seats
        """
        res = [0]*n 
        for in_seat,out_seat, num in bookings:
            res[in_seat-1] += num 
            if out_seat < n :
                res[out_seat] -= num 
            #res[out_seat] -= num 
        for ind in range(1,n):
            res[ind] += res[ind-1]
        return res 


