'''
给定 N 个人的出生年份和死亡年份，第 i 个人的出生年份为 birth[i]，死亡年份为 death[i]，实现一个方法以计算生存人数最多的年份。

你可以假设所有人都出生于 1900 年至 2000 年（含 1900 和 2000 ）之间。如果一个人在某一年的任意时期处于生存状态，那么他应该被纳入那一年的统计中。例如，生于 1908 年、死于 1909 年的人应当被列入 1908 年和 1909 年的计数。

如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。

 

示例：

输入：
birth = {1900, 1901, 1950}
death = {1948, 1951, 2000}
输出： 1901


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/living-people-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 公交车上车、下车方法（出生 = 上车， 死亡 = 下车），计算哪个站点人最多








class Solution(object):
    def maxAliveYear(self, birth, death):
        """
        :type birth: List[int]
        :type death: List[int]
        :rtype: inti
        遍历出现的年份，看该年份出生日期<=该年份 <= 死亡日期，即生存了。
        """
        
        allyear = set(birth + death)
        tmp = dict()
        for year in allyear:
            for ind in range(len(birth)):
                if birth[ind] <= year <= death[ind]:
                    if year not in tmp:
                        tmp[year] = 1
                    else:
                        tmp[year] += 1 
        # 按照两个值进行排序。 items() = (key,value) , 按照value ,-key的降序排列
        sorted_tmp = sorted(tmp.items(), key = lambda x:(x[1],-x[0]),reverse = True) 
        return sorted_tmp[0][0]
        

