#include <iostream>
using namespace std;

int check(int a)
{
    if(a <= 1)
        return 0;
    else if(a == 2 || a == 3)
        return 1;
    for(int i = 2; i < a; i++)
    {
        if(a % i == 0)
            return 0;
    }
    return 1;
}

int main()
{
   int N; cin >> N;
   int tmp = N;
    if(check(N) == 1)
    cout << N;
    else
   {
    for(int i = 2; i < N; i++) {
        while(tmp % i == 0) {
        tmp /= i;
        cout << i << '\n';
    } 
   }
   }
}