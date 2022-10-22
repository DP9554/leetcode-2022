#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,nums,N):
        ##Your code here
        max_sum = -99999
        curr_sum = 0
        
        if len(nums)==1 and nums[0]<0:
            return nums[0]
        if len(nums)==1 and nums[0]==0:
            return 0

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


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends