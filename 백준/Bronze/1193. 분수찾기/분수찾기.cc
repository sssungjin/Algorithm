#include <iostream>
using namespace std;

int main()
{
    int x; cin >> x;

    int i = 0;
    while(x > 0)
    {
        i++;
        x -= i;
    }
    if(i % 2 == 1)
        cout << 1 - x << "/" << i + x;
    else
        cout << i + x << "/" << 1 - x;
}