class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Initializing max (and min ending) variables - Temporaray counters for finding max subarray product
        max_ending_here = 1
        #Also initializing for min ending in order to account for the product of minimum with negative number might becom max(positive)
        min_ending_here = 1
        max_overall = nums[0]
        
        for i in range(len(nums)):
            max_ending_here_temp = max(max_ending_here*nums[i], min_ending_here*nums[i], nums[i])
            min_ending_here = min( max_ending_here*nums[i], min_ending_here*nums[i], nums[i])     
            max_ending_here =  max_ending_here_temp
            if(max_overall < max_ending_here):
                max_overall = max_ending_here
        return(max_overall)