#include <iostream>
using namespace std;

int weight[50];
int height[50];
int idx[50];

void print_rank(int N)
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if(weight[i] < weight[j] && height[i] < height[j])
            idx[i]++;
        }
    }
    for(int i = 0; i < N; i++)
        cout << idx[i] << " ";
}

int main()
{
    int N;

    cin >> N;
    for(int i = 0; i < N; i++)
    {
        idx[i] = 1;
        cin >> weight[i] >> height[i];
    }
    print_rank(N);
}