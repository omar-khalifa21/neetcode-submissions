#include <unordered_map>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> check;
        for (int i = 0; i < nums.size(); i++) {
            if (check.find(nums[i]) != check.end()) {
                return true;
            } else {
                check[nums[i]] = 1;
            }
        }
        return false;
    }
};
