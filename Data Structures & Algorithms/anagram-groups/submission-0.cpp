#include<unordered_map>
#include<iostream>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> temp;
        vector<vector<string>> ans;

        
        for(string &s : strs){

        vector<int> count(26, 0);
        for(char c : s){
            count[c-'a']++;
        }  

        string key;  

        for(int i: count){
            key+= to_string(i)+"#";

        }
        temp[key].push_back(s);

        }
    

    for(auto it = temp.begin() ; it!= temp.end(); it++ ){
       ans.push_back(it->second);
        
    }

       return ans; 
        
    }
};
