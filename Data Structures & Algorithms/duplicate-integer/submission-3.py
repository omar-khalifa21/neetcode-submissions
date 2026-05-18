class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nummap = {};
        for i in nums:
            if i in nummap:
                return True
            nummap[i] =1   
            
            
        return False        
           




        
        