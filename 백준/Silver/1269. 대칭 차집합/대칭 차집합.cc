#include <iostream>
#include <map>
using namespace std;

int main()
{
    map<int, bool> my;
    int n, m;
    int num;

    cin >> n >> m;
    for(int i = 0; i < n+m; i++) {
        cin >> num;
        if(my[num] == true)
            my.erase(num);
        else
            my[num] = true;
    }
    cout << my.size();

}