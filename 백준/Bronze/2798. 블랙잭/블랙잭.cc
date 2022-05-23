#include <iostream>
using namespace std;

int arr[100];

int sum(int N, int M)
{
    int sum, goal;
    int min = 99999;
    for(int i = 0; i < N - 2; i++)
    {
        for(int j = i + 1; j < N - 1; j++)
        {
            for(int k = j + 1; k < N; k++)
            {
                sum = arr[i] + arr[j] + arr[k];
                if(M - sum < min && M - sum >= 0){
                    min = M - sum;
                    goal = sum;
                }
            }
        }
    }
    return goal;
}

int main()
{
    int N, M;
    cin >> N >> M;

    for(int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    cout << sum(N, M);
}