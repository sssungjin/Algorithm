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
    int M, N;
    cin >> M >> N;
    int sum = 0;
    int min = -1;
    int flag = 0;
    for(int i = M; i <= N; i++)
    {
        if(check(i) == 1) {
            flag++;
            sum += i;
            if(flag == 1)
                min = i;
        }
    }
    if(min == -1)
        cout << min;
    else {
        cout << sum << '\n' << min;
    }
    
}