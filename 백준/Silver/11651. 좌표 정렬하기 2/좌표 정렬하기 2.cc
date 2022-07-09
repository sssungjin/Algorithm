#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if(a.second > b.second)
        return false;
    if(a.second == b.second && a.first > b.first)
        return false;
    else
        return true;
}

int main()
{
    int N; cin >> N;
    pair<int, int> tmp;
    vector<pair<int, int>> arr;
    for(int i = 0; i < N; i++)
    {
        cin >> tmp.first >> tmp.second;
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end(), compare);

    for(int i = 0; i < N; i++)
        cout << arr[i].first << ' ' << arr[i].second << '\n';
}