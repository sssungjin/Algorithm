#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int tri[501][501];
    int dp[501][501] = {0};

    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= i; j++) {
            cin >> tri[i][j];
        }
    }

    dp[1][1] = tri[1][1];
    for(int i = 2; i <= n; i++) {
        for(int j = 1; j <= i; j++) {
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j];
        }
    }
    int max = 0;
    for(int i = 1; i <= n; i++) {
        if(max < dp[n][i])
        max = dp[n][i];
    }
    cout << max;
}
