class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
 
        for i in range(len(nums)):
            tmp = nums[i] - 1
            #cyclick sort
            while 1 <=nums[i] <= len(nums) and nums[i]!=nums[tmp]:
                nums[i], nums[tmp] = nums[tmp], nums[i]
                tmp = nums[i]-1
        #checking for missing
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return (i + 1)
            
        return (len(nums) + 1)