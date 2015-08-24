#include <cstdio>
#include <algorithm>
using namespace std;
#pragma warning (disable : 4996)

char s[51];
int sum[51], f[51][51], dp[51][2501];

int main()
{
	int n, m, t;
	scanf("%d%d%d", &n, &m, &t);
	for (int i = 1; i <= n; i++)
	{
		scanf("%s", s + 1);
		for (int j = 1; j <= m; j++)
			sum[j] = sum[j - 1] + s[j] - '0';
		for (int j = 1; j <= m; j++)
			for (int x = 1; x <= m; x++)
			{
				f[x][j] = 0;
				for (int y = 0; y < x; y++)
				{
					int tmp = sum[x] - sum[y];
					f[x][j] = max(f[x][j], f[y][j - 1] + max(tmp, x - y - tmp));
				}
			}
		for (int j = 1; j <= t; j++)
		{
			int tmp = min(m, j);
			for (int k = 1; k <= tmp; k++)
				dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + f[m][k]);
		}
	}
	int ans = 0;
	for (int i = 1; i <= t; i++)
		ans = max(ans, dp[n][i]);
	printf("%d", ans);
	return 0;
}
