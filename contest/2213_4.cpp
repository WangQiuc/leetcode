#include <map>
#include <vector>
#include <string>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        map<int, int> D[26];
        multiset<int> lens;
        int n = s.size(), m = queryCharacters.size();
        vector<int> ans(m);
        for (int i = 0, j = 0; i < n; i = j)
        {
            while (j < n && s[i] == s[j]) j++;
            lens.insert(D[s[i]-'a'][i] = j-i);
        }
        for (int i = 0; i < m; ans[i++] = *(lens.rbegin())) if (s[queryIndices[i]] != queryCharacters[i])
        {
            int idx = queryIndices[i];
            char c = s[idx];
            // split with left range
            auto [l, ld] = *(prev(D[c-'a'].upper_bound(idx)));
            lens.erase(lens.find(ld));
            if (l != idx) lens.insert(D[c-'a'][l] = idx-l);
            else D[c-'a'].erase(l);
            // split with right range
            if (l + ld > idx + 1) lens.insert(D[c-'a'][idx+1] = l+ld-idx-1);

            c = queryCharacters[i];
            int j = idx, d = 1;
            auto it = D[c-'a'].upper_bound(idx);
            // merge with left range
            if (it != D[c-'a'].begin())
            {
                auto [l, ld] = *prev(it);
                if (l+ld == idx)
                {
                    j = l, d += ld;
                    lens.erase(lens.find(ld));
                    D[c-'a'].erase(l);
                }
            }
            // merge with right range
            if (it != D[c-'a'].end() && it->first == idx+1)
            {
                d += it->second;
                lens.erase(lens.find(it->second));
                D[c-'a'].erase(it->first);
            }
            lens.insert(D[c-'a'][j] = d);
            s[idx] = c;
        }
        return ans;
    }
};