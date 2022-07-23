#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int n, m; cin >> n >> m;
    int cnt = 0;
    string s;
    vector<string> result;
    map<string, bool> list;
    
    for(int i = 0; i < n; i++) {
        cin >> s;
        list.insert(make_pair(s, true));
    }
    for(int i = 0; i < m; i++) {
        cin >> s;
        if(list[s]) {
            result.push_back(s);
            cnt++;
        }
    }
    cout << cnt << '\n';
    sort(result.begin(), result.end());
    for(int i = 0; i < result.size(); i++)
        cout << result[i] << '\n';
}