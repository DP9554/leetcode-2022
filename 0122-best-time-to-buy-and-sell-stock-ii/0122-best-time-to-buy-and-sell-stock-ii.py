class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1,p2 = 0,1
        
        curr = 0
        
        while(p1<p2 and p2< len(prices)):
            if(prices[p1]<prices[p2]):
                curr+=prices[p2] - prices[p1]
            p1+=1
            p2+=1
            
        return curr
        