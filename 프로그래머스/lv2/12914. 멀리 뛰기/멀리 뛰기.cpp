#include <string>
#include <vector>

using namespace std;

long long solution(int n) {
    long long answer = 0;
    long long dp[1234567] = {0, 1, 2, };
    
    for(int i = 3; i <= n; i++) {
        dp[i] = dp[i - 2] + dp[i - 1] % 1234567;
    }
    answer = dp[n] % 1234567;
    return answer;
}

