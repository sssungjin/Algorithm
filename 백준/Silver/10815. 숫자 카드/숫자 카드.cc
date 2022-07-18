#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, temp;
    cin >> N;
    vector<int> vec;
    
    while(N--) {
        cin >> temp;
        vec.push_back(temp);
    }
    sort(vec.begin(), vec.end());
    cin >> N;
    while(N--) {
        cin >> temp;
        cout << binary_search(vec.begin(), vec.end(), temp) << ' ';
    }
}