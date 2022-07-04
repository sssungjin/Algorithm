#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

//sort 는 오름차순 정렬

void avg(int arr[], int N)
{
    double sum = 0;
    for(int i = 0; i < N; i++)
    {
        sum += arr[i];
    }
    cout << floor(sum/N + 0.5) << "\n";
}

void center(int arr[], int N)
{
    sort(arr, arr+N);
    cout << arr[N/2] << "\n";
}

void many(int arr[], int N)
{
    int num[8001] = {0, }; //인덱스 - 4000 한 수가 몇번 나왔는지
    for(int i = 0; i < N; i++)
    {
        num[arr[i]+4000]++;
    }
    int tmp = -5000;
    int ret;
    for(int i = 1; i < 8001; i++)
    {
        if(tmp < num[i]){
            tmp = num[i];
            ret = i - 4000;
        }
    }
    int flag[8001] = {0, };
    int check = 0;
    for(int i = 0; i < 8001; i++)
    {
        if(tmp == num[i]) {
            flag[i] = i;
            check++;
        }
    }
    sort(flag, flag + 8001);
    if (check > 1)
        cout << flag[8000-check+2] - 4000 << "\n";
    else
        cout << ret << "\n";
}

void my_range(int arr[], int N)
{
    sort(arr, arr+N);
    cout << arr[N-1]-arr[0] << "\n";
}

int main()
{
    int N; cin >> N;

    int arr[500000];
    for(int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    avg(arr, N);
    center(arr, N);
    many(arr, N);
    my_range(arr, N);
    
}