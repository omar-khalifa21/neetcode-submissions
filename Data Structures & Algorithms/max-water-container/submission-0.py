class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxrea ,i ,j = 0 ,0, len(heights)-1

        while i<j:
            area= (j-i)*min(heights[i],heights[j])
            maxrea = max(area,maxrea)
            if(heights[i]>heights[j]):
                j-=1
            else:
                i+=1
        return maxrea            


        
