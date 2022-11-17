#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        s = set()
        curr = 0
        for num in arr:
            curr+=num
            if curr==0 or num==0:
                return True
            if (curr in s):
                return True
           
            s.add(curr)
        return False
        ##Your code here
        #arr = [4 2 -3 1 6]
     
        #Return true or false


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends