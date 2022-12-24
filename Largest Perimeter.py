class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        A = len(nums)-1
        perimeter = 0

        while A >= 2:
            if nums[A]<nums[A-1] + nums[A-2]:
                perimeter =nums[A] + nums[A-1] + nums[A-2]
                return perimeter
            A -= 1
            
        return  perimeter