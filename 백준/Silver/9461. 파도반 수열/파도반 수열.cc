#include <iostream>
#include <vector>
using namespace std;

vector<long long> dp = {0, 1, 1};

void wave(int n)
{
    for(int i = 3; i <= n; i++) {
        long long tmp = dp[i-3] + dp[i-2];
        dp.push_back(tmp);
    }
}

int main() {
    int t; cin >> t;
    wave(100);
    while(t--){
        int a; cin >> a;
        cout << dp[a] << '\n';
    }
    
    
}