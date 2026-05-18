#include<unordered_map>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> numies;
        priority_queue<pair<int,int>> pq;
        vector<int> result;
        
     
        for (int num : nums) {
            numies[num]++;
        }

         for (auto &p : numies) {
            pq.push({p.second, p.first}); 
            
        }
        
          for (int i = 0; i < k; i++) {
            result.push_back(pq.top().second); 
            pq.pop();
        }

        return result;
    }
};
