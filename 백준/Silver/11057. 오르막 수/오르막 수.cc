#include <stdio.h>

int main()
{
	int N;
	int sum = 0;
	int dp[1001][10] = {0,};
	

	scanf("%d", &N);

	for (int i = 0; i < 10; i++)
		dp[1][i] = 1;
	for (int i = 2; i <= N; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			for (int k = j; k <= 9; k++)
			{
				dp[i][j] += dp[i - 1][k] % 10007;
			}
			
		}
			
	}
	for (int i = 0; i < 10; i++)
		sum =  (sum + dp[N][i]) % 10007;

	printf("%d", sum);
	return 0;
}