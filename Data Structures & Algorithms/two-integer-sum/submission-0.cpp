#include<unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> diff;
        for(int i=0 ; i<nums.size();i++){
            int complement = target-nums[i];

         if (diff.find(complement)!= diff.end())  {
            return {diff[complement], i};

         } 

         diff[nums[i]]=i;


        }
return{};
       

        
     
    }
};
