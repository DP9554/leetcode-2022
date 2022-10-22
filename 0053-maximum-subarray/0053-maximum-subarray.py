class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = -99999
        curr_sum = 0
        if len(nums)==1 and nums[0]<0:
            return nums[0]

        cnt = 0
        for num in nums:
            if num>0:
                break
            cnt+=1
        if cnt == len(nums):
            return sorted(nums)[-1]
            
        for num in nums:
            curr_sum+=num
            
            if curr_sum<0:
                curr_sum = 0
            
            max_sum = max(curr_sum, max_sum)
        
        return max_sum
        