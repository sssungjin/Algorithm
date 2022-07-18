#include <iostream>
#include <cmath>
using namespace std;

bool check(int num)
{
    if(num < 2)
        return false;
    int a = (int)sqrt(num);
    for(int i = 2; i <= a; i++)
    {
        if(num % i == 0)
            return false;
    }
    return true;
}

int main()
{
    int T; cin >> T;
    
    for(int i = 0; i < T; i++)
    {
        int num; cin >> num;
        for(int j = num/2; j >= 2; j--) {
            if(check(j) && check(num-j)) {
                cout << j << " " << num - j << '\n';
                break;
            }
        }
    }
}