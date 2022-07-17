#include <iostream>
#include <cmath>
using namespace std;

int check(int num)
{
    if(num < 2)
        return 0;
    int a = (int)sqrt(num);
    for(int i = 2; i <= a; i++)
    {
        if(num % i == 0)
            return 0;
    }
    return 1;
}

int main()
{
    int n;
    int cnt = 0;
    while(1) {
        cin >> n;
        if(n == 0)
            break;
        for(int i = n+1; i <= 2*n; i++) {
            if(check(i) == 1)
                cnt++;
        }
        cout << cnt << '\n';
        cnt = 0;
    }
}