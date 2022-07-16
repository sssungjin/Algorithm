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
    int arr[100];
    int num = 0;
    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        if(check(a) == 1)
            num++; 
    }
    cout << num;
}