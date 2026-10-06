class Solution:
    def trap(self, height: List[int]) -> int:
        ##Dp (precomputing l_max and r_max arrays)

        n=len(height);water=0
        #creating the l_max and r_max arrays
        l_max=[0]*n;r_max=[0]*n
        
        l_max[0]=height[0]
        #computing l_max
        for i in range(1,n):
            l_max[i]=max(l_max[i-1],height[i])
       # print(l_max)

        r_max[n-1]=height[n-1]
        #computing r_max
        for i in range(n-2,-1,-1):
            r_max[i]=max(r_max[i+1],height[i])
        #print(r_max)

        for i in range(n):
            mini=min(l_max[i],r_max[i])
            water+=mini-height[i]
        
        return water