#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int i, int j)
{
    return j < i;
}

int main()
{
    int num; cin >> num;
    int arr[10];
    int tmp = num;
    int a = 0;

    while(tmp > 0)
    {
        arr[a] = tmp % 10;
        tmp = tmp / 10;
        a++;
    }

    sort(arr, arr+a, compare);
    
    for(int i = 0; i < a; i++)
    {
        cout << arr[i];
    }
}