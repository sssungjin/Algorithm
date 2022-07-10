#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int N; cin >> N;
    int tmp;
    vector<int> vec;
    vector<int> num;
    for(int i = 0; i < N; i++)
    {
        cin >> tmp;
        vec.push_back(tmp);
        num.push_back(tmp);
    }
    sort(vec.begin(), vec.end());
    vec.erase(unique(vec.begin(), vec.end()), vec.end());

    for(int i = 0; i < N; i++)
        cout << lower_bound(vec.begin(), vec.end(), num[i]) - vec.begin() << ' ';
    
    

}