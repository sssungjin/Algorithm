#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
using namespace std;

bool compare(pair<int, string> a, pair<int, string> b)
{
    return a.first < b.first; //b가 크면 true a크면 false
}

int main()
{
    int N; cin >> N;
    pair<int, string> tmp;
    vector<pair<int, string>> arr;
    for(int i = 0; i < N; i++) 
    {
        cin >> tmp.first >> tmp.second;
        arr.push_back(tmp);
    }

    stable_sort(arr.begin(), arr.end(), compare);

    for(int i = 0; i < N; i++)
        cout << arr[i].first << ' ' << arr[i].second << '\n';
    
}