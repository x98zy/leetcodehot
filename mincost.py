#https://leetcode-cn.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/


class Solution:
    def minCost(self, s: str, cost):
        s_temp=""
        res=0
        for i in range(len(s)):
            if s_temp=="" or s_temp[-1]!=s[i]:
                s_temp+=s[i]
            else:
                min_cos=min(cost[i],cost[i-1])
                res+=min_cos
                if min_cos==cost[i]:
                    s_temp=s[0:i]
                    #此处cost[i]改为cost[i-1]是避免cost[i]重复计算
                    cost[i]=cost[i-1]
                else:
                    s_temp=s[0:i-1]+s[i]
        return res

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ret=0
        length=len(s)
        i=0
        while i<length:
            ch=s[i]
            maxvalue=0
            total=0
            while i<length and s[i]==ch:
                maxvalue=max(maxvalue,cost[i])
                total+=cost[i]
                i+=1
            ret+=(total-maxvalue)
        return ret