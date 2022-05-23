#include <stdio.h>

int main()
{
	int N;
	long long dp[91] = {0, 1, };

	scanf("%d", &N);

	for (int i = 2; i <= N; i++)
	{
		dp[i] = dp[i - 2] + dp[i - 1];
	}
	printf("%lld", dp[N]);

	return 0;
}