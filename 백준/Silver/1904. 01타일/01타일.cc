#include <iostream>
#include <vector>
using namespace std;

vector<long long> dp = {0, 1, 2};
int n;

void tiling()
{
    long long tmp;
    for(int i = 3; i <= n; i++) {
        tmp = 0;
        tmp = dp[i-1] + dp[i-2];
        dp.push_back(tmp%15746);
    }
}
int main()
{
    cin >> n;
    tiling();
    cout << dp[n]%15746;
}