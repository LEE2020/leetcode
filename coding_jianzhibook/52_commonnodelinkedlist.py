'''
输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = 0 
        len_b = 0 
        nodea = headA
        nodeb = headB
        while nodea:
            len_a += 1
            nodea =  nodea.next 
        while nodeb:
            len_b += 1
            nodeb = nodeb.next 
        headlong = headA 
        headshort = headB 
        len_diff= len_a - len_b 
        if (len_a < len_b):
            headlong = headB
            headshort = headA
            len_diff = len_b - len_a 
        for ind in range(len_diff):  
            headlong = headlong.next # 先将headshort lenth = headlong lenth ，两个链表的长度一致
        while headshort and headlong and headshort != headlong :
            headshort = headshort.next
            headlong = headlong.next 
        # 此时 headlong 和 headshort 均指向同一个节点
        return headlong
