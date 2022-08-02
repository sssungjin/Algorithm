#include <iostream>
using namespace std;

int series[100001], dp[100001] = {0,};

int main()
{
    int n; cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> series[i];
        dp[i] = series[i];
    }

    int maxSum = dp[0];
    for(int i = 1; i < n; i++) {
        dp[i] = max(dp[i], dp[i-1] + series[i]);
        if(dp[i] > maxSum) {
            maxSum = dp[i];
        }
    }
    cout << maxSum;
}