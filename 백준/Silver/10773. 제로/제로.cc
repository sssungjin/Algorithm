#include <iostream>
using namespace std;

int arr[100001] = {0,};
int s = 0;

void push(int x)
{
    arr[s] = x;
    s++;
}

void pop()
{
    s--;
}

int main()
{
    int N; cin >> N;
    int sum = 0;
    while(N--) {
        int a; cin >> a;
        if(a == 0) {
            pop();
        }
        else {
            push(a);
        }
    }
    for(int i = 0; i < s; i++)
    {
        sum += arr[i];
    }
    cout << sum;

}