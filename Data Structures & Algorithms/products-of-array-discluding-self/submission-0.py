class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       res = [1]*len(nums)
       n = len(nums) 
       pref =1
       for i in range(n):
        res[i]=pref
        pref*=nums[i]

       post =1 

       for i in range(n-1,-1,-1):
        res[i]*= post
        post*= nums[i]
       

       return res  

    
           
             


        