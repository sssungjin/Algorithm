#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare_str(string a, string b)
{
    if(a.length() == b.length())
        return a < b;
    return a.length() < b.length();
}


int main()
{
    int N; cin >> N;
    vector<string> vec;
    for(int i = 0; i < N; i++) {
        string str;
        cin >> str;
        if(find(vec.begin(), vec.end(), str) == vec.end())
        vec.push_back(str); // find해서 중복 없으면 str을 벡터에 삽입
    }
    sort(vec.begin(), vec.end(), compare_str);
    
    for(int i = 0; i < vec.size(); i++) {
        cout << vec[i] << "\n";
    }
}