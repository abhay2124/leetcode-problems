class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        total_even, total_odd = 0, 0
        for i in range(n):
            if i % 2 == 0:
                total_even += nums[i]
            else:
                total_odd += nums[i]
        
        left_even, left_odd = 0, 0
        count = 0
        
        for i in range(n):
            if i % 2 == 0:
                right_even = total_even - left_even - nums[i]
                right_odd = total_odd - left_odd
            else:
                right_even = total_even - left_even
                right_odd = total_odd - left_odd - nums[i]
            
            if left_even + right_odd == left_odd + right_even:
                count += 1
            
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]
        
        return count