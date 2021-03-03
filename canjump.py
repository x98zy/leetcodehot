#https://leetcode-cn.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        max_distince=0
        for i in range(len(nums)):
            if i>max_distince:
                return False
            max_distince=max(max_distince,i+nums[i])
        return True