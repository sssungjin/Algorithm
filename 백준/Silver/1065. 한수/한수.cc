#include <iostream>
using namespace std;

int arr[4];

void divide(int a)
{
    int i = 0;
    while(a > 0)
    {
        arr[i] = a % 10;
        a /= 10;
        i++;  
    }
}

int han(int a)
{
    int cnt = 0;
    if (a < 100)
        cnt = a;
    else
    cnt = 99;
    for(int i = 100; i <= a; i++)
    {
        divide(i);
        if((arr[2] - arr[1] == arr[1] - arr[0]) && i != 1000)
            cnt++;
    }
    return cnt;    
}

int main()
{
    int num;
    
    cin >> num;
    cout << han(num) << endl;

    return 0;
}