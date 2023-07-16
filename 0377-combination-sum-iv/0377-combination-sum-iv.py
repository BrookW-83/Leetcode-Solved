class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def helper(nums, target, c):
            if c in dp:
                return dp[c]
            if c < 0:
                return 0
            if c == 0:
                return 1
            curr = 0
            for i in nums:
                curr += helper(nums, target, c-i)
            dp[c] = curr
            
            return curr
        
        return helper(nums,target,target)