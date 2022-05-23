#include <stdio.h>

int tile(int num)
{
	int dp[1000];

	dp[0] = 1;
	dp[1] = 1;
	for (int i = 2; i <= num; i++)
	{
		dp[i] =( dp[i - 1] + dp[i - 2]) % 10007;
	}
	return dp[num];
}

int main()
{
	int n;
	scanf("%d", &n);

	printf("%d\n", tile(n));
	return 0;
}

