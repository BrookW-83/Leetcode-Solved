class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = float('inf')
        n = len(nums)
        
        for i in range(n-2):
            left, right = i+1, (n - 1)
            
            while left < right:
                close_sum = nums[i] + nums[left] + nums[right]
                
                if close_sum < target:
                    left += 1
                else:
                    right -= 1
                    
                if abs(close_sum - target) < abs(close - target):
                    close = close_sum
                    
        return close
                    
                    
                    