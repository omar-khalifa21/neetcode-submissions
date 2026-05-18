#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char,int> s1;

        for (int i = 0; i < s.size(); i++) {
            s1[s[i]]++;
            s1[t[i]]--;
        }

        for (auto &p : s1) {
            if (p.second != 0) {
                return false;
            }
        }
        return true;
    }
};
