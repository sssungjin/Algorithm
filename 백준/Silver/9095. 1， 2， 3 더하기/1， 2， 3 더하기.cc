#include <stdio.h>

void sum(int num);

int main()
{
	int N;
	int num;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &num);
		sum(num);
	}
	return 0;
}

void sum(int num) {
	int dp[12];
	dp[0] = 1;
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;
	if (num < 4)
	{
		printf("%d\n", dp[num]);
		return;
	}
	else
	{
		for (int i = 4; i <= num; i++)
		{
			dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];
		}
		printf("%d\n", dp[num]);
	}
}