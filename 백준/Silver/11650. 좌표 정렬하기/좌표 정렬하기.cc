#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

struct position {
    int x, y;
};

bool compare(position a, position b)
{
    if(a.x > b.x)
        return false;
    if(a.x == b.x && a.y > b.y)
        return false;
    else
        return true;
}
int main()
{
    int N; 
    cin >> N;
    struct position arr[100001];
    for(int i = 0; i < N; i++)
    {
        scanf("%d %d", &arr[i].x, &arr[i].y);
    }

    sort(arr, arr + N, compare);

    for(int i = 0; i < N; i++)
        printf("%d %d\n", arr[i].x, arr[i].y);
}