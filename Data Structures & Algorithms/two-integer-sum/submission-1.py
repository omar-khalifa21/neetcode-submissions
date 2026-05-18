class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i in range(len(nums)):
           comp = target-nums[i]
           if comp in nummap:
            return[nummap[comp],i]
           nummap[nums[i]]=i 