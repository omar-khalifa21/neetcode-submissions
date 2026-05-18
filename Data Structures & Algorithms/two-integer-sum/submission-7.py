class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numap = {}

        for i in range(len(nums)):

            if target - nums[i] in numap:
                return [numap[target - nums[i]], i]

            numap[nums[i]] = i