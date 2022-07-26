#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    map<string, int> poc_name;
    map<int, string> poc_num;
    int n, m; cin >> n >> m;
    int num = 1;

    for(int i = 0; i < n; i++)
    {
        string tmp; cin >> tmp;
        poc_name.insert({tmp, num});
        poc_num.insert({num++, tmp});
    }
    
    for(int i = 0; i < m; i++)
    {
        char order[21]; cin >> order;
        if(order[0] < 'A')
        {
            int tmp = atoi(order);
            cout << poc_num[tmp] << '\n';
        }
        else
            cout << poc_name[order] << '\n';
    }
}