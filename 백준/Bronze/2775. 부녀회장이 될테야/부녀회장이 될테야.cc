#include <iostream>
using namespace std;

int getnum(int k, int n)
{
    if(n == 1)
        return 1;
    if(k == 0)
        return n;

    return (getnum(k - 1, n) + getnum(k, n-1));    
}
int main()
{
    int count;
    cin >> count;

    for(int i = 0; i < count; ++i)
    {
        int k, n;
        cin >> k >> n;
        cout << getnum(k, n) << '\n';
    }
}